from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json
import products_dao
import orders_dao
import uom_dao
from sql_connection import get_sql_connection

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({'product_id': product_id})
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    return response

@app.route('/deleteOrder', methods=['POST'])
def delete_order():
    return_id = orders_dao.delete_order(connection, request.form['order_id'])
    response = jsonify({'order_id': return_id})
    return response

@app.route('/updateProduct', methods=['POST'])
def update_product():
    return_id = products_dao.update_product(connection, request.form['product_id'], request.form['name'], request.form['price_per_unit'])
    response = jsonify({'product_id': return_id})
    return response

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Grocery Store Management System")
#     app.run(host='0.0.0.0', port=5000)  # Ensure Flask listens on all available IPs
from waitress import serve

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System with Waitress")
    serve(app, host='0.0.0.0', port=5000)
