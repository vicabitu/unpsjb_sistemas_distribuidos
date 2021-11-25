#!/usr/bin/python3
import cgi, cgitb
from http import cookies
import os

# from sqlalchemy.sql.functions import user
from db_handler import Database
import logging
from model import User
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)
metadata = MetaData()
metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

logger = logging.getLogger()

def session_init_render():
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
        </head>
        <body>
            <div>                        
                <form id="login_form" action="/cgi-bin/login.py" method="post">
                    <div>
                        <label for="num">Username::</label>
                        <input type="text" id="username" name="username"><br><br>
                    </div>
                    <div>
                        <label for="password">Password:</label>
                        <input type="password" id="password" name="password"><br><br>
                    </div>
                    <div>
                        <button type="submit" value="Submit" class="btn btn-success">Iniciar sesion</button>
                    </div>
                </form>
            </div>
        </body>
    </html>
    """)

def mofidy_user_render(user):
    name = user.name
    age = user.age
    id = user.id
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
                        <input type="text" value="{id}" class="form-control" id="id_modify_user" name="id_modify_user" aria-describedby="id" placeholder="id">
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

def get_user(id):
    return session.query(User).filter(User.id == id).first()

if __name__ == "__main__" :
    if 'HTTP_COOKIE' in os.environ:
        logger.error("Tengo cookie")
        cookie = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
        logger.error(cookie)

        query_params = os.environ.get("QUERY_STRING").split("&")
        id = query_params[2]
        logger.error(query_params)
        user = get_user(id.split('id=')[1])

        if cookie is None:
            logger.error("Cookie is none")
            session_init_render()

        key = cookie.get('session_key').value if cookie.get('session_key') else ""
        value = cookie.get('session_value').value if cookie.get('session_value') else ""

        database = Database.instance()
        if not database.exists_cookie(key, value):
            logger.exception('Error cookie not in database')
            session_init_render()
        else:
            # Tengo cookies, tengo que mostrar el modal o la pantalla de editar usuario
            logger.error("Tengo cookies")
            mofidy_user_render(user)
    else:
        logger.exception('el environment no tiene la cookie')
        session_init_render()
