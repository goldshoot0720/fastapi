from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
from myappwritedb import list_documents_by_name_part
import json

inventory = APIRouter() 

@inventory.get("/", summary="List inventory(庫存)")
async def inventory_get():
  result = list_documents(collection_id="6876282f0003d93246fe")
  return result

@inventory.get("/{name}")
async def get_inventory_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="6876282f0003d93246fe")
        return result
    except Exception as e:
        return {"error": str(e)}

@inventory.get("/search/{name}")
async def get_inventory_by_name(name: str):
    try:
        result = list_documents_by_name_part(name, collection_id="6876282f0003d93246fe")
        return result
    except Exception as e:
        return {"error": str(e)}