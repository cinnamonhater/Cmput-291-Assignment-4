def main():
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbEmbed"]
    mycol = mydb[tracks]
    myquery = {//query in here}
    mydoc = mycol.find(myquery)
    pass

if __name__ == "__main__":
    main()
