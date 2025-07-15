from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

subscription = APIRouter()

@subscription.get("/", summary="List subscription")
async def subscription_get():
  result = list_documents(collection_id="687250d70020221fb26c")
  return result

@subscription.get("/{name}")
async def get_subscription_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="687250d70020221fb26c")
        return result
    except Exception as e:
        return {"error": str(e)}