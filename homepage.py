from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def homepage():
#     return "<p>Hello, World!</p>"


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('main.html', person=name)
