from pymongo import MongoClient
# import datetime, pymongo
from pprint import pprint
from bson.objectid import ObjectId


CLIENT = MongoClient("mongodb://localhost:27017/")
mongo_db = CLIENT["culturecaremongodb"]


forms_collection = mongo_db["forms_collection"]


def insert_into_forms_collection(**kwargs):
    """
    Add record to forms_collection
    """
    form = {
        "type" : kwargs.get("type"),
        "body" : kwargs.get("body"),
        "deleted" : False
    }

    try:
        form_id = forms_collection.insert_one(form).inserted_id
    except:
        return False, None
    
    return True, str(form_id)
