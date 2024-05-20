from pymongo import MongoClient

user = 'root'
password = 'MTAyODctamFtZXNj' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host='localhost'

#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select a database named training.
trainingdb = connection.training

# select a collection named mongodb_glossary.
glossarycoll = trainingdb.mongodb_glossary

# insert documents into the collection mongodb_glossary.
documents =[
    {"database":"a database contains collections"},
    {"collection":"a collection stores the documents"},
    {"document":"a document contains the data in the form of key value pairs."}
]


glossarycoll.insert_many(documents)

glossarydocs = glossarycoll.find()
print("All documents in the collection")
for doc in glossarydocs:
    print(doc)

# close the server connecton
print("Closing the connection.")
connection.close()