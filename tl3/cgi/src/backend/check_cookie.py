#!/usr/bin/python3
import os
import json
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from db_handler import Database
from model import User
from http import cookies

db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)
metadata = MetaData()
metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

logger = logging.getLogger()

try:
    if 'HTTP_COOKIE' in os.environ:
        # Viene la cookie en la cabecera
        cookie = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])

        if cookie is None:
            logger.error("No hay cookie")

        key = cookie.get('session_key').value
        value = cookie.get('session_value').value
        database = Database.instance()

        if not database.exists_cookie(key, value):
            logger.error("La cookie no existe en la base de datos")
        else:
            cookie = database.get_cookie(key)
            print("Content-Type: application/json;charset=utf-8")
            print()
            user_db = session.query(User).filter(User.username == key, User.password == value).first()
            response = {
                'name': user_db.name,
                'username': user_db.username,
                'age': user_db.age,
                'password': user_db.password
            }
            print(json.JSONEncoder().encode(response))
    else:
        logger.error("No vino la cookie")
except Exception as e:
    logger.error(f"Error: {e}")