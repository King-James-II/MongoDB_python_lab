from pymongo import MongoClient

user = 'root'
password = 'MTAyODctamFtZXNj' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host='localhost'

#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 
trainingdb = connection.training

# select the 'python' collection 
pycollection = trainingdb.python

# insert a sample document
document = {"test":"test1", "testing": "testing2"}
trainingdb.pycollection.insert_one(document)

# query for all documents in 'training' database and 'python' collection
alldocs = trainingdb.pycollection.find()

for doc in alldocs:
    print(doc)
