from flask_restful import Resource
from flask import jsonify
from db_connection import command, config


class User(Resource):
    def __init__(self):
        pass

    def post(self):
        return "Hello Flask From User."

    def get(self):
        users = []
        command.execute("select * from users")
        result = command.fetchall();
        for row in result:
            users.append(jsonify(row))
            print(jsonify(row))
        return jsonify(users)


class UserRUD(Resource):
    def __init__(self):
        pass

    def get(self, id):
        return "Hello Flask From User."

    def put(self, id):
        return "Hello Flask From User."

    def delete(self, id):
        return "Hello Flask From User."
