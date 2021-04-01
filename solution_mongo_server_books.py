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
db = client.books_db

# drop the collection if it already exists so here's a clean slate.
db.drop_collection("books")

# grab a reference to a database, access a collection using "db.collectionname"
collection = db.books


# bring in data from csv, format it appropriately
all_books = []
with open('author-text-date.csv') as f:
    data = f.readlines() # list of lines
    data = data[1:-1] #update to not include first list
    for line in data:
        list_of_fields = line.split(',')
        # construct a dictionary with each field
        # author, text, date
        author = list_of_fields[0]
        text = list_of_fields[1]
        date_values = list_of_fields[2].split('-')
        # strings, convert to numbers
        date = datetime.datetime( int(date_values[0]), int(date_values[1]), int(date_values[2]), 12)
        # print(d)
        # grab year, month, day from the date section and format like below
        print(author, text, date)
        # example_date = datetime.datetime(year, month, day, 12) 
        entry = { 
            "author": author,
            "text": text,
            "date": date
        }
        # append that dictionary to the all_books list
        all_books.append(entry)

# check your all_books looks good
print('*********')
print('before db add', all_books)

# insert all_books into the database
db.books.insert_many(all_books)

# make a query to get all books after 2009
print('* Books written after 2009')
print()
d = datetime.datetime(2009, 1, 1, 12)
for book in db.books.find({"date": {"$gt": d}}).sort("author"):
  # all posts will be dates greater than 2001, 
  pprint.pprint(book)
  print()

# verify all books have been added
print('*ALL BOOKS*')
for book in db.books.find():
    pprint.pprint(book)
    print()

# find a document in collection in a few different ways.

# find_one where author is Hemingway

# find all with author "Pen Name"

# query for the count of all books
print("All Books: ", db.books.count_documents({}))
print()
# query for the count of all books by Hemingway
print("Hemmingway Books: ", db.books.count_documents({ "author": "Hemmingway" }))
print() 

# use mongo's "dollar-sign" query operators to get all books after the year 2010
print("Finding books written after the year 2010:")
d = datetime.datetime(2010, 1, 1, 12)
for book in db.books.find({"date": {"$gt": d}}).sort("author"):
  # all posts will be dates greater than 2001, 
  pprint.pprint(book)
  print()
