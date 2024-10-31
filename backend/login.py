from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql, login_flag

auth = Blueprint("auth", __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

def update_failed_attempts(username):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE Customer SET failed_attempts = failed_attempts + 1 WHERE email_ID = %s;", (username,))
    mysql.connection.commit()
    cursor.close()

def reset_failed_attempts(username):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE customer SET failed_attempts = 0 WHERE email_ID = %s;", (username,))
    mysql.connection.commit()
    cursor.close()

def validate_customer(username, password):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Customer_ID FROM customer where email_ID = %s and Password=%s;", (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

def get_blocked(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT blocked FROM customer NATURAL JOIN check_blocked where email_ID = %s;", (username,))
    failed_attempts = cursor.fetchone()
    cursor.close()
    if failed_attempts is None:
        return False
    return failed_attempts[0]


def DropTriggerLogin(username):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE Customer SET failed_attempts = failed_attempts + 1 WHERE email_ID = %s;", (username,))
    mysql.connection.commit()
    cursor.close()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        failed_attempts = get_blocked(email)

        if failed_attempts:
            flash('Your account is locked due to too many failed login attempts. Please contact support at SportSwiftDB@gmail.com.', 'error')            
            return redirect(url_for('auth.login'))

        customer = validate_customer(email, password)
        if customer:
            session["customer_ID"] = customer
            reset_failed_attempts(email)
            login_flag = True
            return redirect(url_for('home'))  
        else:
            DropTriggerLogin(email)
            flash('Invalid username or password','alert')
            return redirect(url_for('auth.login'))
    return render_template('login.html')  
