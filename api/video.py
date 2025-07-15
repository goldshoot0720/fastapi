from fastapi import APIRouter

video = APIRouter()

@video.get("/",summary="video get summary",description="video get description")
async def video_get():
  return {"video":"video"}
