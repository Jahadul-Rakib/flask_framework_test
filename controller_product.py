from flask_restful import Resource


class Product(Resource):
    def __init__(self):
        pass

    def post(self):
        return "Hello Flask From Product."

    def get(self):
        return "Hello Flask From Product."


class ProductRUD(Resource):
    def __init__(self):
        pass

    def get(self, id):
        return "Hello Flask From Product."

    def put(self, id):
        return "Hello Flask From Product."

    def delete(self, id):
        return "Hello Flask From Product."
