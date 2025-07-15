from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

bank = APIRouter()

@bank.get("/", summary="List bank")
async def bank_get():
  result = list_documents(collection_id="6875df530018459b05b6")
  return result

@bank.get("/{name}")
async def get_bank_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="6875df530018459b05b6")
        return result
    except Exception as e:
        return {"error": str(e)}