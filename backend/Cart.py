from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql

Cart = Blueprint("Cart", __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@Cart.route('/cart/delete/<int:product_id>', methods=['POST'])
def delete_from_cart(product_id):
    if "customer_ID" in session:
        customer_ID = session["customer_ID"]
        delete_product_from_cart(customer_ID, product_id)
        flash('Product removed from cart.', 'success')
    return redirect(url_for('Cart.cart'))

def delete_product_from_cart(customer_id, product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM Cart WHERE Customer_ID = %s AND Product_ID = %s", (customer_id, product_id))
    mysql.connection.commit()
    cursor.close()

def fetch_products(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product WHERE Product_ID IN (SELECT Product_ID FROM Cart WHERE Customer_ID = %s)", (customer_id,))
    products = cursor.fetchall()
    cursor.close()
    return products

@Cart.route('/cart', methods=['GET'])
def cart():
    customer_ID = None
    products = []
    if "customer_ID" in session:
        customer_ID = session["customer_ID"]
        products = fetch_products(customer_ID)
    return render_template('cart.html', products=products)

    
