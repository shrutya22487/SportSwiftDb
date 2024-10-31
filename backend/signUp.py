from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql, login_flag

signUp = Blueprint("signUp", __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

def exists(email):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Customer_ID FROM customer where email_ID = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    return user

def register(name, email, password, address):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("START TRANSACTION")
        cursor.execute("INSERT INTO customer (Name, email_ID, Password, Address) VALUES (%s, %s, %s, %s)", (name, email, password, address))
        cursor.execute("COMMIT")
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
    
    cursor.close()

@signUp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Name = request.form['Name']
        email = request.form['email']
        password = request.form['password']
        Address = request.form['Address']

        if exists(email):
            flash('email already taken!')
            return redirect(url_for('signUp.signup'))  
        else:
            register(Name, email, password, Address)
            return redirect(url_for('auth.login'))
    return render_template('signup.html')  
