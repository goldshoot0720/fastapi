from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

routine = APIRouter()

@routine.get("/", summary="List routine")
async def routine_get():
  result = list_documents(collection_id="68725b3000111e8852b1")
  return result

@routine.get("/{name}")
async def get_routine_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="68725b3000111e8852b1")
        return result
    except Exception as e:
        return {"error": str(e)}