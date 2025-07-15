from fastapi import APIRouter

subscription = APIRouter()

@subscription.get("/",summary="subscription get summary",description="subscription get description")
async def subscription_get():
  return {"subscription":"subscription"}

@subscription.get("/{name}",summary="subscription get by name summary",description="subscription get by name description")
async def subscription_get_by_name(name):
  return {"subscription":name}
