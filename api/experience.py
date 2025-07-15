from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

experience = APIRouter()

@experience.get("/", summary="List experience")
async def experience_get():
  result = list_documents(collection_id="6875eeea0023af204d34")
  return result

@experience.get("/{name}")
async def get_experience_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="6875eeea0023af204d34")
        return result
    except Exception as e:
        return {"error": str(e)}