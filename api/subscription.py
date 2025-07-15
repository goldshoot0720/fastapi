from fastapi import APIRouter

subscription = APIRouter()

@subscription.get("/",summary="subscription get summary",description="subscription get description")
async def subscription_get():
  return {"subscription":"subscription"}
