from fastapi import APIRouter

mail = APIRouter()

@mail.get("/",summary="mail get summary",description="mail get description")
async def mail_get():
  return {"mail":"mail"}
