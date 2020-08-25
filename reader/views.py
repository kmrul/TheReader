from reader import app

@app.route('/hello')
def hello():
    return "<h1>Hello Flask </h1>"