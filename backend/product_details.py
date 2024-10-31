from flask import render_template, jsonify, Blueprint
from app import mysql, login_flag

product_details = Blueprint("product_details", __name__)

@product_details.route('/<int:product_id>')
def product_detail(product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product WHERE Product_ID = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    return render_template('product_detail.html', product=product)

@product_details.route('/getProduct/<int:product_id>')
def get_product(product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product WHERE Product_ID = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    return jsonify(product_detail)
