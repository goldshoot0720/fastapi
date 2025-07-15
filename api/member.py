from fastapi import APIRouter

member = APIRouter()

@member.get("/",summary="member get summary",description="member get description")
async def member_get():
  return {"member":"member"}
