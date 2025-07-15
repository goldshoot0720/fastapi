from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

host = APIRouter()

@host.get("/", summary="List host")
async def host_get():
  result = list_documents(collection_id="687251cc000e150d16da")
  return result

@host.get("/{name}")
async def get_host_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="687251cc000e150d16da")
        return result
    except Exception as e:
        return {"error": str(e)}