import pymongo
import demo_20_netEase_1_crawler

class Database:
    host = 'localhost'
    port = 27017
    client = None
    db_name = None
    database = None
    collection = None
    
    def __init__(self, database_name="NetEase-Music"):
        self.db_name = database_name
        return

    def start(self):
        self.client = pymongo.MongoClient(self.host, self.port)
        self.database = self.client[self.db_name]
        return self.database

    def collection(self,collection_name):
        return self.database[collection_name]
    
    def switch_collection(self, collection_name):
        self.collection = self.database[collection_name]
        return self
    
    def close(self):
        self.client.close()
        return 

    def list_collection_names(self, ptn=True):
        name_s = self.database.list_collection_names()
        if (ptn):
            for name in name_s: print(name)
        return list(name_s)




def main():
    crawler = x 
    return

    database = Database()
    database.start()

    collection_user     = database.collection("user")
    collection_user.insert_one({"user": "init_user"})
    collection_playlist = database.collection("playlist")
    collection_playlist.insert_one({"playlist": "init_playlist"})
    collection_song     = database.collection("song")
    collection_song.insert_one({"song": "init_song"})

    database.list_collection_names()

    database.close()


if __name__ == "__main__":
    main()

