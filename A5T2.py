from pymongo import MongoClient
from bson.json_util import loads

def getData(name):

    with open(name, encoding="utf8") as file:
        data = loads(file.read())
    return data

def embedData(artists, tracks):

    #go through each artist and using its track 
    for i in range(len(artists)):
        #for each artist check their 'tracks' and fetch their data
        for j in range(len(artists[i]['tracks'])):
            track_id = artists[i]['tracks'][j]
            #for each of their tracks go through all of the tracks and replace their id with their full data
            for track in tracks:
                if(track['track_id'] == track_id):
                    artists[i]['tracks'][j] = track

    return artists

def main():

    file_names                  = ["artists.json", "tracks.json"]
    client                      = MongoClient('mongodb://localhost:27017')
    db_name                     = "A4dbEmbed"
    database                    = client[db_name]
    artists_tracks_collection   = database[file_names[0][:-5] + file_names[1][:-5]]
    artists_tracks              = embedData(getData(file_names[0]), getData(file_names[1]))
    artists_tracks_collection.insert_many(artists_tracks)

if __name__ == "__main__":
    main()