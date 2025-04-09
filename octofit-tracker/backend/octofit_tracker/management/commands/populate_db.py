from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Populate collections with test data
        for collection_name, data in test_data.items():
            collection = db[collection_name]
            collection.delete_many({})  # Clear existing data
            collection.insert_many(data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data.'))
