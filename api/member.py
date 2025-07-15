from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

member = APIRouter()

@member.get("/", summary="List member")
async def member_get():
  result = list_documents(collection_id="6875ede80000cbabf57e")
  return result

@member.get("/{name}")
async def get_member_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="6875ede80000cbabf57e")
        return result
    except Exception as e:
        return {"error": str(e)}