from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from app import mysql, login_flag

Cart = Blueprint("Cart", __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@Cart.route('/cart/delete/<int:product_id>', methods=['POST'])
def delete_from_cart(product_id):
    if "customer_ID" in session:
        customer_ID = session["customer_ID"]
        delete_product_from_cart(customer_ID, product_id)
        flash('Product removed from cart.', 'success')
    return redirect(url_for('Cart.cart'))

@Cart.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if "customer_ID" in session:
        customer_ID = session["customer_ID"]
        quantity = int(request.form['quantity'])
        add_product_to_cart(customer_ID, product_id, quantity)
        flash('Product added to cart.', 'success')
   
    return redirect(url_for('Cart.cart'))

def delete_product_from_cart(customer_id, product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE Cart SET Deleted = TRUE WHERE Customer_ID = %s AND Product_ID = %s", (customer_id, product_id))
    mysql.connection.commit()
    cursor.close()

def add_product_to_cart(customer_id, product_id, quantity):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO Cart (Customer_ID, Product_ID, Quantity) VALUES (%s, %s, %s)", (customer_id, product_id, quantity))
    mysql.connection.commit()
    cursor.close()
    
def fetch_products(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT Product.*, Cart.Quantity
        FROM Product
        JOIN Cart ON Product.Product_ID = Cart.Product_ID
        WHERE Cart.Customer_ID = %s AND Cart.Deleted = FALSE
    """, (customer_id,))
    products = cursor.fetchall()
    cursor.close()
    return products


@Cart.route('/cart', methods=['GET'])
def cart():
    customer_ID = session.get("customer_ID")
    if not customer_ID:
        flash('Please log in to view your cart.', 'alert')
        return redirect(url_for('auth.login'))  # Assuming 'auth.login' is your login endpoint

    products = fetch_products(customer_ID)
    return render_template('cart.html', products=products)
