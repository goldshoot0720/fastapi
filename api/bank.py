from fastapi import APIRouter

bank = APIRouter()

@bank.get("/",summary="bank get summary",description="bank get description")
async def bank_get():
  return {"bank":"bank"}
