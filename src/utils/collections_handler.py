import json
import os

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
        "name": name,
        "url": url,
        "method": method,
        "headers": headers,
        "body": body
    })

    with open(collections_file, "w") as file:
        json.dump(collections, file, indent=4)

def get_collection_names():
    """Returns a list of collection names."""
    return [entry["name"] for entry in load_collections()]

def get_collection_by_name(name):
    """Returns a collection by name."""
    for entry in load_collections():
        if entry["name"] == name:
            return entry

    return None

def delete_collection(name):
    collections = load_collections()
    collections = [entry for entry in collections if entry["name"] != name]
    with open(collections_file, "w") as file:
        json.dump(collections, file, indent=4)