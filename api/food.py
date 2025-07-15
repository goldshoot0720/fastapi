from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

food = APIRouter()

@food.get("/", summary="List food")
async def food_get():
  result = list_documents(collection_id="6868f512003b1abedb72")
  return result

@food.get("/{name}")
async def get_food_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="6868f512003b1abedb72")
        return result
    except Exception as e:
        return {"error": str(e)}