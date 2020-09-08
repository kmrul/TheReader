from flask import render_template, redirect, url_for, request
from reader import app

from .models import User

@app.route('/user', methods=['GET', 'POST'])
def user():

    return render_template('user/user.html')


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    
    return render_template('user/add-user.html')