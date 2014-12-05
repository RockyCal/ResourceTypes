__author__ = 'Raquel'

from pymongo import MongoClient

client = MongoClient()

db = client.resourceTypes
types = db.types

#for doc in types.find():
#    print(doc)

# Helper function for adding synonyms to document dictionary
def update_doc(doc, synonyms):
    doc['synonyms'] = synonyms.split(', ')
    return doc


name = input("Enter the name of a resource type to modify: ")

search = types.find_one({'name': name})

if search is not None:
    new_synonyms = input("Enter synonyms of this resource type, separated by a comma: ")
    new_doc = update_doc(types.find_one({'name': name}), new_synonyms)
    types.update({'name': name}, new_doc)