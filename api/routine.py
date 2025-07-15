from fastapi import APIRouter

routine = APIRouter()

@routine.get("/",summary="routine get summary",description="routine get description")
async def routine_get():
  return {"routine":"routine"}
