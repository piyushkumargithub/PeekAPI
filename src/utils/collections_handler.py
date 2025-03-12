import json
import os
import uuid

collections_file="collections.json"

def load_collections():
    """Loads collections from the database."""
    if not os.path.exists(collections_file):
        return []

    with open(collections_file, "r") as file:
        return json.load(file)
    
def save_collection(name,url,method,headers,body):
    """Saves a collection to the database."""
    collections = load_collections()
    collections.append({
        "id": str(uuid.uuid4()), # unique ID
        "name": name,
        "url": url,
        "method": method,
        "headers": headers,
        "body": body
    })

    with open(collections_file, "w") as file:
        json.dump(collections, file, indent=4)


def get_collection_by_id(collection_id):
    """Finds a collection by its unique ID."""
    collections = load_collections()
    for entry in collections:
        if entry["id"] == collection_id:
            return entry
    return None


def delete_collection(collection_id):
    """Deletes a collection by ID instead of name."""
    collections = load_collections()
    collections = [entry for entry in collections if entry["id"] != collection_id]

    with open(collections_file, "w") as file:
        json.dump(collections, file, indent=4)