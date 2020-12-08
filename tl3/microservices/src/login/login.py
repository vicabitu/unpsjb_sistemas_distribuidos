from flask import (
    Flask, 
    render_template, 
    make_response, 
    jsonify, 
    request,
)
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from db_handler import Database

"""
Flask related definitions
"""
app = Flask(__name__)

PORT = 5000
HOST = '0.0.0.0'

db = Database.instance()


@app.route("/", methods = ['POST', 'GET'])
def index():

    if request.method == 'GET':
        print('INDEX || GET ')
        print('INDEX || GET || test user query')
        print(get_users())
        return render_template("login.html")

    if request.method == 'POST':
        print('INDEX || POST ')
        print(request)
        user = request.form['username']
        password = request.form['password']
        # resp = make_response(render_template('login.html', result = result))
        resp = make_response(render_template('login.html'))
        resp.set_cookie('userID', user)
        resp.set_cookie('userPASS', password)

        return resp


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
   
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    
    return resp


@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'


@app.route("/template")
def hola():
    return render_template("login.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


@app.route("/json")
def get_json():
    print("LOGIN || get_json || init ")
    data = {"user": "pedro"}
    return make_response(jsonify(data), 200)


@app.route("/users/<user>")
def get_user(user):    
    data = {"user": user}
    return make_response(jsonify(data), 200)


@app.route("/users", methods=["POST"])
def post_user():    
    print(" === LOGIN || post_user ")        
    for i in dir(request):
        print(i)
    print(request.get_data())
    req = request.get_json()
    return make_response(jsonify(req), 200)   


if __name__ == '__main__':
    print(f"Login microservice runnning in port {PORT}")
    app.run(host=HOST, port=PORT, debug=True)
