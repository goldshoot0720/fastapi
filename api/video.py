from fastapi import APIRouter
from myappwritedb import list_documents
from myappwritedb import list_documents_by_name
import json

video = APIRouter()

@video.get("/", summary="List video")
async def video_get():
  result = list_documents(collection_id="686beea30020d8ea151f")
  return result

@video.get("/{name}")
async def get_video_by_name(name: str):
    try:
        result = list_documents_by_name(name, collection_id="686beea30020d8ea151f")
        return result
    except Exception as e:
        return {"error": str(e)}