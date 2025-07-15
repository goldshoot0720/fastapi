from fastapi import APIRouter

host = APIRouter()

@host.get("/",summary="host get summary",description="host get description")
async def host_get():
  return {"host":"host"}
