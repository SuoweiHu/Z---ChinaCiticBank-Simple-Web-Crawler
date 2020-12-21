# -*- coding: utf-8 -*-


import pymongo
import datetime
import pprint
from bson.objectid import ObjectId # This is for converting the objectID for the docuemnt from str type of objectId type 

# Official Document: 
#       https://pymongo.readthedocs.io/en/stable/tutorial.html


def main():

    # ================================
    # Pre Step-up
    # MongoClient 
    client = pymongo.MongoClient()   # Create a MongoClient to the running mongod instance 
    # client = MongoClient('localhost', 27017)                      # Localhost and port version
    # client = pymongo.MongoClient('mongodb://localhost:27017/')    # URI Formatt version

    # Database 
    db = client.myNewDatabase        # Access database via the MongoClient instance
    # db = client['test-database']   # (Another version of the same functionality)

    # Collection
    myNewDatabase_db = db.myNewDatabase   #  Getting the collection via the database 
                                # A collecion is a group of document stored in MongoDB 
                                # (is about quivalant to a table in the relational database)
    # collection = db['test-collection']  # (Another version of the same functionality)
    posts = db.posts
    users = db.users 

    # ================================
    # List collection names 

    # Noting that in PyMongo, dictionay is ued to represent document 
    # (in mongoDB data are represented and stored using JSON style documents)

    name_s = db.list_collection_names()
    print('=' * 100)
    print("The Database has the following collections:")
    for name in name_s: print('\t-[ ' + name + ' ]')
    print('=' * 100)


    # ================================
    # Date Operation - Insertion

    # Inserting single document
    bool_ptn_insertSingleDoc = False
    if(bool_ptn_insertSingleDoc):
        mydict = {               
            'like_num': '100', 
            'title': 'mongodb', 
            'type': 'data', 
            'time': '2018-3-14', 
            'read_num': '1000', 
            'name': 'dwzb', 
            'comment_num': '0'}
        dict_id = myNewDatabase_db.insert_one(mydict).inserted_id
        post = {"author": "Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}
        post_id = posts.insert_one(post).inserted_id

        user_1 = {
            "user_id" : "u6966666",
            "name"    : "Simon Hamston",
            "name_abbriv" : "SH",
            "dob" : "2000.00.00",
            "password" : "password"
        }
        user_2 = {
            "user_id" : "u69777777",
            "name"    : "Cath Dollson",
            "name_abbriv" : "CD",
            "dob" : "1999.00.00",
            "password" : "password"
        }
        user_id_1 = users.insert_one(user_1).inserted_id
        user_id_2 = users.insert_one(user_2).inserted_id
        print(dict_id)
        print(post_id)
        print(user_id_1)
        print(user_id_2)

    # Inserting multiple document 
    bool_ptn_insertMultiDoc = False
    if(bool_ptn_insertMultiDoc):
        user_3 = {
            "user_id" : "u69788888",
            "name"    : "Porter Hitman",
            "name_abbriv" : "PH",
            "dob" : "1900.00.00",
            "password" : "password"
        }
        user_4 = {
            "user_id" : "u699999999",
            "name"    : "Doom Destorier",
            "name_abbriv" : "DD",
            "dob" : "1899.00.00",
            "password" : "password"
        }
        user_5 = {
            "user_id" : "u7000000000",
            "name"    : "Sage Hasake",
            "name_abbriv" : "SH",
            "dob" : "2000.00.00",
            "password" : "password"
        }
        user_docs = [user_3, user_4, user_5]
        user_id_s = users.insert_many(user_docs).inserted_ids
        print(user_id_s)
    
    print('=' * 100)

    # ================================
    # Date Operation - Querying

    # Querying over single document
    bool_ptn_singleDocumentQuery = False
    if(bool_ptn_singleDocumentQuery):
        # Finding the very first document of the "users" collection
        print("First doc of \'User\' collection:")
        pprint.pprint(users.find_one()) 
        print('-' * 40)
        # FInding the specific docuemnt that has matching with some {attribute : value}
        print("Doc of name abbriviation \'SH\':")
        pprint.pprint(users.find_one({"name_abbriv":"SH"}))
        print('-' * 40)
        # Finding the specific document that has ObjectId (attribute "_id" by default)
        print("Doc of ObjectID of " + str(user_id_2))
        pprint.pprint(users.find_one({"_id":ObjectId(user_id_2)}))
        print('-' * 40)

    # Querying for more than one document (record)
    bool_ptn_multiDocumentQuery = False
    if(bool_ptn_multiDocumentQuery):
        # Finding all the student of name abbriviation of SH
        print("Doc of name abbriviation \'SH\':")
        for student in users.find({"name_abbriv":"SH"}):
            pprint.pprint(student)
        print('-' * 40)
        # Counting the number of student that was born at 2000.00.00
        count_num = users.count_documents({"dob":"2000.00.00"})
        print("There are a totoal of {} student born at 2000.00.00".format(count_num))
        
    print('=' * 100)

    # ================================
    # Date Operation - Indexing 
    final_exam = db['2400-final-exam']

    # Show current indexing for the collection 
    bool_ptn_showIndex = False
    if bool_ptn_showIndex:
        index_s = sorted(list(final_exam.index_information()))
        print(index_s)

    # First lets make some mock data into the database 
    bool_ptn_indexingAccountID = True
    if(bool_ptn_indexingAccountID):
        # Collection : 2400-final-exam
        # Create index on the user_id attribute

        # ========
        # WARNING: THIS PART WILL THORW AND ERROR IF DATA ALREADY EXISTS 
        # ========

        final_exam.create_index([('user_id', pymongo.ASCENDING)], unique=True)
        result_s = [
            {"user_id":"u696633", "score":"3"},
            {"user_id":"u696644", "score":"4"},
            {"user_id":"u696611", "score":"1"},
            {"user_id":"u696622", "score":"2"},
            {"user_id":"u696600", "score":"0"}
        ]
        result_id_s = final_exam.insert_many(result_s).inserted_ids
        print(result_id_s)

    # ================================
    # Wrapping up
    client.close() # Close of the MongoClient
    


if __name__ == "__main__":
    main()
