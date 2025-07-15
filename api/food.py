from fastapi import APIRouter

food = APIRouter()

@food.get("/",summary="food get summary",description="food get description")
async def food_get():
  return {"food":"food"}
