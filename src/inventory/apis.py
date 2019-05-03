from flask_restful import Resource
from core import api


class InventoryResource(Resource):
    """
    Inventory API
    """
    def get(self):
        print("Hello - Inventory.")
        return "Hello - Inventory."

    def post(self):
        print("Hello - Inventory.")
        return "Hello - Inventory."

api.add_resource(InventoryResource, '/')
