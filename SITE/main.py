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

# --- 1. CONFIGURATION SOCKET.IO & FASTAPI ---
# 'async_mode=asgi' bach i-khdem m3a FastAPI
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI(title="ESTBM AI & Real-Time Chat Engine")
# Inclure le router d'authentification
app.include_router(auth_router)
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

# --- 3. CHAT REAL-TIME LOGIC ---
# Dictionary bach n-3erfou chkoun li online (Apogee -> Session ID)
connected_users = {}

@sio.event
async def join(sid, data):
    apogee = data.get('apogee')
    connected_users[apogee] = sid
    print(f"L-user {apogee} t-connecta (SID: {sid})")

@sio.event
async def send_private_msg(sid, data):
    # data fiha: sender, receiver, content
    receiver_id = data.get('receiver')
    
    print(f"Message de {data.get('sender')} à {receiver_id}: {data.get('content')}")
    
    # Ila l-receiver online, n-siftou lih l-message f l-blast (room) dyalo
    if receiver_id in connected_users:
        target_sid = connected_users[receiver_id]
        await sio.emit('receive_private_msg', data, room=target_sid)

# --- 4. RUN SERVER ---
if __name__ == "__main__":
    # Darouri n-lanciwo 'socket_app' machi 'app'
    uvicorn.run(socket_app, host="127.0.0.1", port=8000)