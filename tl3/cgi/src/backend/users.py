#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import sqlalchemy
import logging
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

cgitb.enable()

logger = logging.getLogger()

print("Content-Type: application/json;charset=utf-8")
print()

db_string = "postgres://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)

metadata = MetaData()

metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    age = Column(Integer)
    password = Column(String)

    def __init__(self, name, age, username, password):
        self.name = name
        self.age = age
        self.username = username
        self.password = password


def query_users():
    users = []
    for u in session.query(User).all():
        user = u.__dict__
        user.pop('_sa_instance_state', None)    
        users.append(user)
    logger.error("gettinhg userss ==================")
    logger.error(type(users))
    logger.error(users)
    users = {
        "password": "un_password", 
        "username": "pedro", 
        "id": 1, 
        "age": 36, 
        "name": "Pedro Konstantinoff"
    }
    return users


def create_user():
    try:
        form = cgi.FieldStorage()
        user = User(
            form.getvalue('name'),
            form.getvalue('age'),
            form.getvalue('username'),
            form.getvalue('password')
            )
        session.add(user)
        session.commit()
        return {'error': False}
    except:
        return {'error': True}
    

if os.environ['REQUEST_METHOD'] == 'GET':
    response = query_users()    
if os.environ['REQUEST_METHOD'] == 'POST':
    response = create_user()
if not response:
    response = {}


print(json.JSONEncoder().encode(response))