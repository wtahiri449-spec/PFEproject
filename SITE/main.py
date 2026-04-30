import uvicorn
import socketio
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# Importer le router d'authentification
from app.routes.auth import router as auth_router
from app.database import SessionLocal, init_db
from app.models import Message
from app.database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# --- 1. CONFIGURATION SOCKET.IO & FASTAPI ---
# 'async_mode=asgi' bach i-khdem m3a FastAPI
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI(title="ESTBM AI & Real-Time Chat Engine")
# Inclure le router d'authentification
app.include_router(auth_router)

init_db()

from fastapi.staticfiles import StaticFiles
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models import User

# Mount static files (HTML, JS, CSS) from the current directory
app.mount("/", StaticFiles(directory=".", html=True), name="static")

socket_app = socketio.ASGIApp(sio, app)

# Configuration CORS (Bach l-Frontend i-hder m3a l-Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



# --- 2. MACHINE LEARNING MODELS (Analyse AI) ---
# Data d l-entrainement (Notes S1, Note S2, Absences)
X_train = np.array([
    [16, 15, 0], [14, 13, 2], [10, 11, 5], 
    [8, 7, 12], [18, 17, 1], [11, 10, 3],
    [12, 12, 2], [9, 10, 8], [15, 14, 0]
])

# Label Regression (Note S3)
y_reg = np.array([15.8, 13.5, 10.2, 7.5, 17.8, 10.5, 12.1, 9.2, 14.8])
model_reg = LinearRegression().fit(X_train, y_reg)

# Label Classification (0=Risque, 1=Admis, 2=Excellent)
y_class = np.array([2, 1, 1, 0, 2, 1, 1, 0, 2])
model_forest = RandomForestClassifier(n_estimators=50).fit(X_train, y_class)

class StudentInput(BaseModel):
    s1: float
    s2: float
    absences: int

@app.post("/predict_all")
async def predict_performance(data: StudentInput):
    features = np.array([[data.s1, data.s2, data.absences]])
    
    # 1. Prédire la Note (Regression)
    pred_note = model_reg.predict(features)[0]
    
    # 2. Prédire la Catégorie (Random Forest)
    res_class = int(model_forest.predict(features)[0])
    labels = {0: " Risque (Attention)", 1: "Admis (Bon travail)", 2: " Admis (Excellent)"}
    
    return {
        "regression_note": round(float(pred_note), 2),
        "random_forest": labels[res_class]
    }

@app.get("/messages/{user1}/{user2}")
def get_conversation(user1: str, user2: str, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(
        ((Message.sender_apogee == user1) & (Message.receiver_apogee == user2)) |
        ((Message.sender_apogee == user2) & (Message.receiver_apogee == user1))
    ).order_by(Message.timestamp.asc()).all()
    result = []
    for m in messages:
        # Get sender's full name from User table
        sender_user = db.query(User).filter(User.apogee == m.sender_apogee).first()
        sender_name = sender_user.full_name if sender_user else m.sender_apogee
        result.append({
            "sender": m.sender_apogee,
            "receiver": m.receiver_apogee,
            "content": m.content,
            "timestamp": m.timestamp.isoformat(),
            "senderName": sender_name
        })
    return result
# --- 3. CHAT REAL-TIME LOGIC ---
connected_users = {}       # apogee -> sid
user_info = {}             # apogee -> {"is_prof": bool, "name": str}

def get_online_users_list():
    users = []
    for apogee, info in user_info.items():
        users.append({
            "apogee": apogee,
            "name": info["name"],
            "is_prof": info["is_prof"]
        })
    return users

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def disconnect(sid):
    apogee_to_remove = None
    for apogee, s in connected_users.items():
        if s == sid:
            apogee_to_remove = apogee
            break
    if apogee_to_remove:
        del connected_users[apogee_to_remove]
        user_info.pop(apogee_to_remove, None)
        await sio.emit('online_users_update', get_online_users_list())

@sio.event
async def join(sid, data):
    apogee = data.get('apogee')
    is_prof = data.get('is_prof', False)
    name = data.get('name', apogee)
    if not apogee:
        print("Join missing apogee, ignoring")
        return
    connected_users[apogee] = sid
    user_info[apogee] = {"is_prof": is_prof, "name": name}
    print(f"User {apogee} ({'Prof' if is_prof else 'Student'}) connected: {name}")
    await sio.emit('online_users_update', get_online_users_list())

@sio.event
async def get_online_users(sid):
    await sio.emit('online_users_update', get_online_users_list(), room=sid)

@sio.event
async def send_private_msg(sid, data):
    sender = data.get('sender')
    receiver = data.get('receiver')
    content = data.get('content')
    if not all([sender, receiver, content]):
        return
    # Save to database
    db = SessionLocal()
    try:
        msg = Message(sender_apogee=sender, receiver_apogee=receiver, content=content)
        db.add(msg)
        db.commit()
    finally:
        db.close()
    # Forward to receiver if online
    if receiver in connected_users:
        target_sid = connected_users[receiver]
        await sio.emit('receive_private_msg', data, room=target_sid)
    # Echo back to sender (so it appears in their chat)
    await sio.emit('receive_private_msg', data, room=sid)