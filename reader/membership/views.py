from flask import render_template, request, redirect, url_for
from reader import app

@app.route('/membership')
def membership():
    return render_template('membership/membership.html')