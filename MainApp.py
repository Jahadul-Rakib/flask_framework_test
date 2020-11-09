from flask import Flask
from flask_restful import Api

from controller_user import User, UserRUD
from controller_product import Product, ProductRUD

# app initialize
app = Flask(__name__)
api = Api(app)

# request router
api.add_resource(User, '/user')
api.add_resource(UserRUD, '/user/<int:id>')

api.add_resource(Product, '/product')
api.add_resource(ProductRUD, '/product/<int:id>')

# app start run from main method
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloder=True)
