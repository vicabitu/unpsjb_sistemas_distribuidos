#!/usr/bin/python3
import cgi
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

def get_script_set_cookie(username, password):
    logger.error("get_script")
    script = "<script>"
    script += "$(document).ready(function() {"
    script += f"Cookies.set('session_key', '{username}');"
    script += f"Cookies.set('session_value', '{password}');"
    script += "});"
    script += "</script>"
    return script

def mofidy_user_render(user):
    username = user.username
    password = user.password
    name = user.name
    age = user.age
    print()
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Login</title>
            <script type="text/javascript" src="../statics/jquery-3.5.1.js"></script>
            <script type="text/javascript" src="../statics/bootstrap/js/bootstrap.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.min.js" type="text/javascript"></script>
            <script src="https://cdn.jsdelivr.net/npm/js-cookie@beta/dist/js.cookie.min.js"></script>
            <link rel="stylesheet" href="../statics/bootstrap/css/bootstrap.min.css">
            <link rel="stylesheet" href="../statics/estilos.css">
            {get_script_set_cookie(username, password)}
        </head>
        <body>
            <div <div class="content">           
                <h1>Modificar usuario</h1>
                <form id="modify_user" action="/cgi-bin/modify_user.py" method="post">
                    <div class="form-group">
                        <label for="name">Nombre</label>
                        <input type="text" value="{name}" class="form-control" id="name_modify" name="name_modify_user" aria-describedby="emailHelp" placeholder="Nombre">
                    </div>
                    <div class="form-group">
                        <label for="age">Edad</label>
                        <input type="text" value="{age}" class="form-control" id="age_modify" name="age_modify_user" placeholder="Edad">
                    </div>
                    <div hidden class="form-group">
                        <label for="user_id">Usuario</label>
                        <input type="text" class="form-control" id="id_modify" name="id_modify_user" aria-describedby="id" placeholder="id">
                    </div>
                    <div class="form-group">
                        <button type="submit" value="Submit" class="btn btn-success">Guardar</button>
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                    </div
                </form>
            </div>
        </body>
    </html>
    """)

try:
    database = Database.instance()
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    user = login(username, password)
    if user:
        logger.error("If de login")
        if not database.exists_cookie(username, password):
            database.insert_cookie(username, password)
        mofidy_user_render(user)
    else:
        logger.error("No existe el usuario")
except Exception as e:
    logger.error(f"Error: {e}")