import pymongo
client=pymongo.MongoClient("mongodb+srv://Swetha27:1234@cluster0.vo4jt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.get_database('CSBS')
collection=db.office_details

for x in collection.find():
    print(x)