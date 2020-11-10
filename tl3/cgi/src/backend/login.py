#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import logging 
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

cgitb.enable()

logger = logging.getLogger()
print("Content-Type: application/json;charset=utf-8")
print()

response = {'success':'true','message':'The Command Completed Successfully'}
print(json.JSONEncoder().encode(response))