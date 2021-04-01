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
# dont use hyphens for db name
db = client.books_db

# drop the collection if it already exists so here's a clean slate.
db.drop_collection("books")

# grab a reference to a database, access a collection using "db.collectionname"
collection = db.books


# bring in data from csv, format it appropriately
all_books = []
with open('author-text-date.csv') as f:
    data = f.readlines() # list of lines
    for line in data:
        list_of_fields = line.split(',')
        # construct a dictionary with each field
        # author, text, date
        # author = 
        # text = 
        # grab year, month, day from the date section and format like below
        # date = need to format like the following, include 12 to zero out hours
        # example_date = datetime.datetime(year, month, day, 12) 
        # entry = { } this should have author, text, date fields w/ values you grabbed above
        # append that dictionary to the all_books list

# check your all_books looks good
print(all_books)

# insert all_books into the database
# db.books.insert_many(pass the books in here)

# make a query to get all books after 2009
#db.books.find(check out the example we did before in the readme)

# verify all books have been added

# find a document in collection in a few different ways.

# find_one where author is Hemingway

# find all with author "Pen Name"

print("Verifying all books created:")

# Add several blog posts to the collection at once using .insert_many()

# query for the count of all books

# query for the count of all books by Hemingway

# use mongo's "dollar-sign" query operators to get all books after the year 2010
print("Finding blog posts after the year 2010:")
d = datetime.datetime(2010, 1, 1, 12)


# the sky is the limit, can you now write to a file all books by 'Pen Name'?
# feel free to try bringing in other csv files, and creating corresponding db's with them.

