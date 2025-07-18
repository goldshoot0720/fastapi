from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

mail = APIRouter()

@mail.get("/", summary="List mail")
async def mail_get():
  result = list_documents(collection_id="687a15df000014dff513")
  return result

@mail.get("/{name}")
async def get_mail_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="687a15df000014dff513")
        return result
    except Exception as e:
        return {"error": str(e)}