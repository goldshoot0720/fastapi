from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

article = APIRouter()

@article.get("/", summary="List article")
async def article_get():
  result = list_documents(collection_id="687fdfd70003cf0e3f97")
  return result

@article.get("/{name}")
async def get_article_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="687fdfd70003cf0e3f97")
        return result
    except Exception as e:
        return {"error": str(e)}