import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template("Assign2.html")

@app.route('/School')
def open_school():
    return flask.render_template("School.html")

@app.route('/Work')
def open_work():
    return flask.render_template("Work.html")

@app.route('/Hobbies')
def open_hobbies():
    return flask.render_template("Hobbies.html")

@app.route('/home')
def open_home():
    return flask.render_template("Assign2.html")

if __name__ == '__main__':
    app.run()