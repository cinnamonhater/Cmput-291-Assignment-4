from pymongo import MongoClient


def dropCOllections(database, names):

    for name in names:
        database.drop_collection(name[:-5])

def getData(name):

    with open(name) as file:
        print("FIle opened? :O")
        data = file.read()
    data = data.replace("$oid", "ObjectId")
    file.close()
    return eval(data)

def main():
    file_names = ["artists.json", "tracks.json"]
    #https://docs.mongodb.com/manual/administration/install-community/
    #USE VERSION 3.7.0 NOT 4 of mongodb
    #https://pymongo.readthedocs.io/en/stable/tutorial.html

    client = MongoClient('mongodb://localhost:27012')
    db_name = "A4dbNorm"
    database = client[db_name]
    artists_collection = database[file_names[0][:-5]]
    tracks_collection  = database[file_names[1][:-5]]
    collections = database.list_collection_names()
    for name in (file_names):
        if(name[:-5] in collections):
            print(f"collection already '{name[:-5]}' exists")

    artists = getData(file_names[0])
    tracks  = getData(file_names[1])
    database = dropCOllections(database, file_names)

    


if __name__ == "__main__":
    main()