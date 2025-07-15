from appwrite.client import Client
from appwrite.services.databases import Databases

# 初始化 Appwrite client
client = Client()
client.set_endpoint("https://fra.cloud.appwrite.io/v1")  # ✅ 改成你的 endpoint
client.set_project("680c76af0037a7d23e44")               # ✅ 改成你的 Project ID
client.set_key("standard_26a62ae02136189303edd7cac4614a1d712c789e0bfd95f751e7876c10e9afd429b696938cb63dda958d6e1a1660c5653842ff12a9d9673434bf747d9642c73e53baf296246330c05f0561d2bba08070ccbe6e17bb522e1ad2eb0dc6d5473aa8fe162691900b70be38b177af62b44105a36b916757339159620f9a77aba96143")                  # ✅ 改成你的 API Key

# 正確定義 database
database = Databases(client)

# 資料庫 ID
DATABASE_ID = "680c778b000f055f6409"

# ✅ List 所有 documents
def list_documents(collection_id: str):
    return database.list_documents(
        database_id=DATABASE_ID,
        collection_id=collection_id
    )

# ✅ 完全比對 name
def list_documents_by_name(name: str, collection_id: str):
    return database.list_documents(
        database_id=DATABASE_ID,
        collection_id=collection_id,
        queries=[
            f'equal("name", ["{name}"])'
        ]
    )

# ✅ 模糊比對 name
def list_documents_by_name_part(name: str, collection_id: str):
    return database.list_documents(
        database_id=DATABASE_ID,
        collection_id=collection_id,
        queries=[
            f'search("name", "{name}")'
        ]
    )

# ✅ Update amount（你會用到的）
def update_document(document_id: str, collection_id: str, data: dict):
    return database.update_document(
        database_id=DATABASE_ID,
        collection_id=collection_id,
        document_id=document_id,
        data=data
    )
