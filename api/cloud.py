from fastapi import APIRouter

cloud = APIRouter()

@cloud.get("/",summary="cloud get summary",description="cloud get description")
async def cloud_get():
  return {"cloud":"cloud"}
