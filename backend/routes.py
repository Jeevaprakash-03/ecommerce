from flask import Blueprint, jsonify
from db import get_connection

routes = Blueprint("routes", __name__)

@routes.route("/products", methods=["GET"])
def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)
