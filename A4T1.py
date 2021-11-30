from pymongo import MongoClient

def main():
    file_names = ["artists.json", "tracks.json"]
    # Use client = MongoClient('mongodb://localhost:27017') for specific ports!
    client = MongoClient('mongodb://localhost:27017')
    db_name = "A4dbNorm"
    database = client[db_name]
    artists_collection = database[file_names[0][:-5]]
    tracks_collection  = database[file_names[1][:-5]]
    collections = database.list_collection_names()
    for name in (file_names):
        if(name[:-5] in collections):
            print(f"collection '{name}' exists")

    print(collections)

if __name__ == "__main__":
    main()