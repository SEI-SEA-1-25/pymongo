# Using PyMongo

## Objectives

- [ ] Use PyMongo to a MongoDB database
- [ ] Create blogposts
- [ ] Review PyMongo API documentation ( [here](https://pymongo.readthedocs.io/en/stable/) )
- [ ] Import a csv, and add those values to a mongo database

## Connect to MongoDB

We will be using a Python library called **PyMongo** to connect to and interact with MongoDB. You can use this with frameworks like Flask (a python equivalent of express), or just on it's own. You'll find that PyMongo is "pythonic" in that it's easy to use and it's designed to be readable. The syntax it uses almost seems like you're writing inside the Mongo shell itself. Oh and another thing, we are not in the synchronous JS world, so there will be no callback, `async`/`await` or `.then` promise hassle.

First, use `pip3` in your terminal to install PyMongo.

```text
$ pip3 install pymongo
```

Remember to start your local MongoDB server:
It might already be running.

```text
$ mongo
```

**mongo-server.py**:

```python
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
client = MongoClient()
db = client.test_database

# drop the collection if it already exists so here's a clean slate.
db.drop_collection("blogposts")

# grab a reference to a database, access a collection using "db.collectionname"
collection = db.blogposts

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

# insert one blog post to the collection.
post_id = db.blogposts.insert_one(post1).inserted_id

# verify the blog post has been added.
# find a document in collection in a few different ways.
db.blogposts.find_one()
db.blogposts.find_one({"author": "Guido"})
retrieved_post = db.blogposts.find_one({"_id": post_id})

print("Verifying Guido's post was created:")
pprint.pprint(retrieved_post)
print()

# Add several blog posts to the collection at once using .insert_many()
db.blogposts.insert_many([post2, post3])

# query for several blogposts
print("Finding all blog posts:")
for post in db.blogposts.find():
  pprint.pprint(post)
print()

print("Total posts:", db.blogposts.count())
print("Total posts by Guido:", db.blogposts.find({"author": "Guido"}).count())
print()

# use mongo's "dollar-sign" query operators
print("Finding blog posts after the year 2000:")
d = datetime.datetime(2000, 1, 1, 12)
for post in db.blogposts.find({"date": {"$gt": d}}).sort("author"):
  pprint.pprint(post)
```

Ok. Now your turn. You are going to be working in mongo_server_books.py.

We want you to read in the `csv` in the repo, and add each line into your `books` database. This will take some work to format it correctly, when you are done getting it into place, do some queries as outlined in the file to test your `pymongo` knowledge. We will do this in groups of 3 - 4.

Refer to MongoDB documentation to find out more details about how to interact with MongoDB through PyMongo.

You'll find that methods are probably called just about what you expect them to be called. Here's some popular methods:

- insert_one
- insert_many
- find_one
- find_many
- fine_one_and_update
- fine_one_and_delete
- update_one
- update_many
- delete_one
- delete_many

Entire API: [http://api.mongodb.com/python/current/api/index.html](http://api.mongodb.com/python/current/api/index.html)

Collection level docs: [http://api.mongodb.com/python/current/api/pymongo/collection.html](http://api.mongodb.com/python/current/api/pymongo/collection.html)
