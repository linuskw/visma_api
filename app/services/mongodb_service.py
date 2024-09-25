import uuid
from datetime import datetime

import pymongo


class MongodbService:
    visma_db = None

    @staticmethod
    def global_init(app):
        client = pymongo.MongoClient(app.config["MONGO_URI"])
        MongodbService.visma_db = client[app.config["MONGO_DB"]]

    @staticmethod
    def delete_one_by_resource(resource, find):
        collection = MongodbService.visma_db[resource]
        return collection.delete_one(find)

    @staticmethod
    def find_by_resource(resource, lookup, sort=[], limit=0):
        collection = MongodbService.visma_db[resource]
        if sort:
            return collection.find(lookup).sort(sort).limit(limit)
        return collection.find(lookup).limit(limit)

    @staticmethod
    def find_one_by_resource(resource, lookup):
        collection = MongodbService.visma_db[resource]
        return collection.find_one(lookup)

    @staticmethod
    def update_one_by_resource(resource, find, data):
        collection = MongodbService.visma_db[resource]
        if "$set" in data:
            data["$set"].update({
                '_updated': datetime.utcnow(),
                '_etag': str(uuid.uuid4()).replace('-', '')
            })
        elif "$inc" in data:
            pass
            # Do nothing
        else:
            data.update({
                '_updated': datetime.utcnow(),
                '_etag': str(uuid.uuid4()).replace('-', '')
            })
        return collection.update_one(find, data)

    @staticmethod
    def insert_one_by_resource(resource, data: dict):
        collection = MongodbService.visma_db[resource]
        data.update({
            '_updated': datetime.utcnow(),
            '_created': datetime.utcnow(),
            '_etag': str(uuid.uuid4()).replace('-', '')
        })
        return collection.insert_one(data)

    @staticmethod
    def update_by_resource(resource, find, data):
        collection = MongodbService.visma_db[resource]
        if "$set" in data:
            data["$set"].update({
                '_updated': datetime.utcnow(),
                '_etag': str(uuid.uuid4()).replace('-', '')
            })
        elif "$inc" in data:
            pass
            # Do nothing
        else:
            data['$set'] = {
                '_updated': datetime.utcnow(),
                '_etag': str(uuid.uuid4()).replace('-', '')
            }
        return collection.update_many(
            filter=find,
            update=data
        )
