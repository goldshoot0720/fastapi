from fastapi import FastAPI
import uvicorn
import threading
import time
import requests
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from api.inventory import inventory
from api.experience import experience
from api.member import member
from api.bank import bank
from api.mail import mail
from api.cloud import cloud
from api.routine import routine
from api.host import host
from api.subscription import subscription
from api.video import video
from api.food import food
app = FastAPI()
# ---- 保活函數 ----
def keep_alive():
    while True:
        try:
            requests.get("https://fastapitsaopaofenghsiung2025.onrender.com/healthcheck")
            print("保活 ping 成功")
        except Exception as e:
            print("保活失敗:", e)
        time.sleep(900)  # 每 15 分鐘

# ---- 啟動時自動啟動保活 ----
@app.on_event("startup")
def startup_event():
    threading.Thread(target=keep_alive, daemon=True).start()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(inventory,prefix="/inventory",tags=["inventory(庫存) tags"])
app.include_router(experience,prefix="/experience",tags=["experience tags"])
app.include_router(member,prefix="/member",tags=["member tags"])
app.include_router(bank,prefix="/bank",tags=["bank tags"])
app.include_router(mail,prefix="/mail",tags=["mail tags"])
app.include_router(cloud,prefix="/cloud",tags=["cloud tags"])
app.include_router(routine,prefix="/routine",tags=["routine tags"])
app.include_router(host,prefix="/host",tags=["host tags"])
app.include_router(subscription,prefix="/subscription",tags=["subscription tags"])
app.include_router(video,prefix="/video",tags=["video tags"])
app.include_router(food,prefix="/food",tags=["food tags"])
@app.get("/")
def app_get():
  return RedirectResponse(url="/docs")
# ---- 健康檢查 ----
@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}
if __name__ == "__main__":
  uvicorn.run("main:app",port=8080,reload=True)
