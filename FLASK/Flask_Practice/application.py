from flask import Flask
from flask import render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/welcome')
def front():
    return "welcome"
 
@app.route("/accessHTML")
def linkhtml():
    return(render_template("home.html"))

@app.route('/home/<name>')
def about(name):
    fruits=["apple","orange"]
    return render_template("home.html",name=name,fruits=fruits)

@app.route('/profile/<username>')
def explore(username):
    return username


