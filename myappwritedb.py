import json
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.query import Query

PROJECT_ID = '680c76af0037a7d23e44'
ENDPOINT = 'https://fra.cloud.appwrite.io/v1'
DATABASE_ID = '680c778b000f055f6409'

client = Client()
client.set_endpoint(ENDPOINT).set_project(PROJECT_ID)
# 如果需要驗證可用 set_key 或 set_session
# client.set_key('你的API密鑰')

databases = Databases(client)

def list_documents(collection_id: str, database_id=DATABASE_ID, queries=None):
    return databases.list_documents(
        database_id=database_id,
        collection_id=collection_id,
        queries=queries or []
    )

def list_documents_by_name(name: str, collection_id: str, database_id=DATABASE_ID):
    return databases.list_documents(
        database_id=database_id,
        collection_id=collection_id,
        queries=[Query.equal("name", name)]
    )

def list_documents_by_name_part(name: str, collection_id: str):
    documents = databases.list_documents(
        database_id=DATABASE_ID,
        collection_id=collection_id,
        queries=[
            Query.contains("name", name)]
    )
    return documents