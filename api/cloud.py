from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

cloud = APIRouter()

@cloud.get("/", summary="List cloud")
async def cloud_get():
  result = list_documents(collection_id="68748996002e640d98d9")
  return result

@cloud.get("/{name}")
async def get_cloud_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="68748996002e640d98d9")
        return result
    except Exception as e:
        return {"error": str(e)}