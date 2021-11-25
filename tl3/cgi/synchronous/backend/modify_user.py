#!/usr/bin/python3
import cgi
import json
import logging
from sqlalchemy import create_engine, MetaData, log
from sqlalchemy.orm import sessionmaker
from model import User

db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)
metadata = MetaData()
metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

logger = logging.getLogger()

def get_user(id):
    return session.query(User).get(id)

def modify_user(user, form):
    user.name = form.getvalue('name_modify_user')
    user.age = form.getvalue('age_modify_user')
    session.commit()

try:
    print("Content-Type: application/json;charset=utf-8")
    print()
    form = cgi.FieldStorage()
    id = form.getvalue('id_modify_user')
    user = get_user(id)
    if user:
        modify_user(user, form)
    else:
        logger.error("No existe el usuario")
        response = {'modify': False}
    response = {'modify': True}
    print(json.JSONEncoder().encode(response))
except Exception as e:
    logger.error(f"Error: {e}")
