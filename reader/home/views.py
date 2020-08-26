from flask import render_template, request, redirect, url_for
from reader import app

@app.route('/home')
def home():
    return render_template('home.html')