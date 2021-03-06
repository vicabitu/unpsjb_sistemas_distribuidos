#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import logging
from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from model import User

cgitb.enable()

logger = logging.getLogger()

print("Content-Type: application/json;charset=utf-8")
print()

db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)
metadata = MetaData()
metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

def query_users():
    users = []
    for u in session.query(User).all():
        # user = u.__dict__
        # user.pop('_sa_instance_state', None)
        createdat = u.createdat.strftime("%Y-%m-%d %H:%M:%S")
        user = {
            "id": u.id,
            "name": u.name,
            "age": u.age,
            "username": u.username,
            "password": u.password,
            "createdat": createdat
        }
        users.append(user)
    return users


def create_user():
    try:
        form = cgi.FieldStorage()
        user = User(
            form.getvalue('name'),
            form.getvalue('age'),
            form.getvalue('username'),
            form.getvalue('password'),
            datetime.now()
        )
        session.add(user)
        session.commit()
        return {'error': False}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {'error': True}
    
if os.environ['REQUEST_METHOD'] == 'GET':
    response = query_users()    
if os.environ['REQUEST_METHOD'] == 'POST':
    response = create_user()
if not response:
    response = {}


print(json.JSONEncoder().encode(response))