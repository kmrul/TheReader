from flask import render_template, request, redirect, url_for
from reader import app

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')