from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    age = Column(Integer)
    password = Column(String)
    createdat = Column(DateTime)

    def __init__(self, name, age, username, password, createdat):
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.createdat = createdat