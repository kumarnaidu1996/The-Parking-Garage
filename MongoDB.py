# Import the required libraries
import os
import pandas as pd
import numpy as np


# Database (MongoDB) class
class Mongodb:

    def __init__(self, db_name='SRH_Berlin_University', table_name='Parking_Data'):
        self.db_name = db_name
        self.table_name = table_name

    # mongoDB database
    def data_upload_to_mongodb(self, record):

        try:
            from pymongo import MongoClient
            client = MongoClient('localhost', 27017)
            db = client[self.db_name]
            collection = db[self.table_name]
            collection.insert_one(record)

        except Exception as e:
            print(e)
