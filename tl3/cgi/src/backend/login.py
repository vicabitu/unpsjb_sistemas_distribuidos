#!/usr/bin/python3
import os
import cgi
import json
import logging 
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger()
print("Content-Type: application/json;charset=utf-8")
print()


form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

response = {'username': username, 'password': password}
print(json.JSONEncoder().encode(response))