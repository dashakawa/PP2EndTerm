import pymongo 
import ssl
#CONNECT TO SERVER
client = pymongo.MongoClient("mongodb://localhost:27017/")
#Database create
mydb = myclient["mydatabase"]

print(myclient.list_database_names())
#printing databases

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")



#creating collection ~ table in SQL
mycol = mydb["customers"]
#Important: In MongoDB, a collection is not created until it gets content!

print(mydb.list_collection_names())
#Return a list of all collections 

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.") 
#specific review collection 

