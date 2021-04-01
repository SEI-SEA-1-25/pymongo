from pymongo import MongoClient

# import datetime so we can have timestamps on things we add to the database.
import datetime

# import pprint so we can pretty print objects from the database.
import pprint

# pymongo connects to the default host and port if you don't specify any
# parameters to the constructor when it's initialized. If you need to connect
# to a non-default MongoDB on your local machine then simply specify the host
# and port:
# host = 'localhost'
# port = 27017
# client = MongoClient(host, port)

# if nothing passed in where does MongoClient look?
client = MongoClient()
db = client.pymongo_test

# what does this do
db.drop_collection("blogposts")

# what does this do
collection = db.blogposts

# what python datatype is this? 
post1 = {
  "author": "Guido",
  "text": "Idea for a Programming Language",
  "tags": ["python", "release", "development"],
  "date": datetime.datetime(1989, 12, 23, 12)
}

post2 = {
  "author": "Mongo Team",
  "text": "Introducing MongoDB!",
  "tags": ["mongodb", "release", "development"],
  "date": datetime.datetime(2009, 11, 12, 12)
}

post3 = {
  "author": "Guido",
  "text": "Using MongoDB, Python and Flask",
  "tags": ["python", "mongodb", "pymongo", "development"],
  "date": datetime.datetime(2012, 2, 5, 12)
}

# what does this do
post_id = db.blogposts.insert_one(post1).inserted_id


# what does this do
db.blogposts.find_one()

# what does this do
retrieved_post = db.blogposts.find_one({"author": "Guido"})
pprint.pprint(retrieved_post)


# note the 12 is for hours, we need datetime vs date to save in mongodb
print(datetime.datetime(2000, 1, 1, 12))
print()

# what does this do?
db.blogposts.insert_many([post2, post3])

# what does this do?
print("")
for post in db.blogposts.find():
  pprint.pprint(post)
print()

# what does count_documents do?
print("", db.blogposts.count_documents({}))
print("", db.blogposts.count_documents({ "author": "Guido" }))
print()


# what does this do?
d = datetime.datetime(2001, 1, 1, 12)
for post in db.blogposts.find({"date": {"$gt": d}}).sort("author"):
  pprint.pprint(post)

