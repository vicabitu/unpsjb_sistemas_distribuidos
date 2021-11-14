#!/usr/bin/python3
import cgi
import json
import logging 
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from db_handler import Database
from model import User

db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)
metadata = MetaData()
metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

logger = logging.getLogger()

def login(username, password):
    return session.query(User).filter(User.username == username, User.password == password).first()

try:
    database = Database.instance()
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    if login(username, password):
        if not database.exists_cookie(username, password):
            database.insert_cookie(username, password)
        print("Content-Type: application/json;charset=utf-8")
        print()
        response = {'username': username, 'password': password}
        print(json.JSONEncoder().encode(response))
    else:
        logger.error("No existe el usuario")
except Exception as e:
    logger.error(f"Error: {e}")