# explore.py
from flask import Blueprint, request, jsonify, render_template
from app import mysql, login_flag

explore_bp = Blueprint("explore", __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@explore_bp.route('/explore')
def explore():
    return render_template('explore.html')

@explore_bp.route('/get_products')
def get_products():
    sport = request.args.get('sport')
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Product WHERE category = %s', (sport,))
    products = cursor.fetchall()
    cursor.close()
    return jsonify({'success': True})

@explore_bp.route('/product_list')
def product_list():
    sport = request.args.get('sport')
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Product WHERE category = %s', (sport,))
    products = cursor.fetchall()
    cursor.close()
    return render_template('product_list.html', products=products)
