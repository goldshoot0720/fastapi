from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
from myappwritedb import list_documents_by_search_name
import json
from myappwritedb import update_document
from fastapi import Body

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
async def get_inventory_by_search_name(name: str):
    try:
        result = list_documents_by_search_name(name, collection_id="6876282f0003d93246fe")
        return result
    except Exception as e:
        return {"error": str(e)}

@inventory.patch("/update/{doc_id}", summary="Update inventory amount")
async def update_inventory_amount(doc_id: str, new_amount: int = Body(...)):
    try:
        result = update_document(
            document_id=doc_id,
            collection_id="6876282f0003d93246fe",
            data={"amount": new_amount}
        )
        return {"message": "Amount updated", "result": result}
    except Exception as e:
        return {"error": str(e)}
