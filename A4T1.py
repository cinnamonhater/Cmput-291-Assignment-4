from pymongo import MongoClient
from bson.json_util import loads

def dropCOllections(database, names):

    for name in names:
        database.drop_collection(name[:-5])

def getData(name):

    with open(name, encoding="utf8") as file:
        data = loads(file.read())
    return data

def main():

    file_names          = ["artists.json", "tracks.json"]
    client              = MongoClient('mongodb://localhost:27017')
    db_name             = "A4dbNorm"
    database            = client[db_name]
    artists_collection  = database[file_names[0][:-5]]
    tracks_collection   = database[file_names[1][:-5]]
    artists             = getData(file_names[0])
    tracks              = getData(file_names[1])
    artists_collection.insert_many(artists)
    tracks_collection.insert_many(tracks)

    #database = dropCOllections(database, file_names) used for testing
if __name__ == "__main__":
    main()