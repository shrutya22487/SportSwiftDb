from flask import render_template, Blueprint
from app import mysql, login_flag

product_list = Blueprint("product_list", __name__,  template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@product_list.route('/products')
def products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()
    cursor.close()
    return render_template('product_list.html', products=products)
