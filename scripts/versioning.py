import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection("versions")

def save_version(text, version_id):
    collection.add(documents=[text], ids=[version_id])
    return f"💾 Saved as version {version_id}"

def get_version(version_id):
    result = collection.get(ids=[version_id])
    return result["documents"][0] if result else None

def list_versions():
    try:
        return collection.get()["ids"]
    except:
        return []
