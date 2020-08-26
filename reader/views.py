from flask import render_template, request, redirect, url_for
from reader import app


@app.route('/')
def index():
    return "<h1>Index</h1>"

@app.route('/success')
def success():
    return "<h1>Data Saved Successfully.</h1>"