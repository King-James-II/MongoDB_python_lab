from pymongo import MongoClient

user = 'root'
password = 'MTAyODctamFtZXNj' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host='localhost'

#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# get database list
print("Getting list of databases")
dbs = connection.list_database_names()

# print the database names
for db in dbs:
    print(db)

# close the server connecton
connection.close()