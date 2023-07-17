import random

from flask import Blueprint, current_app, request
from sqlalchemy.sql import text

departamento = Blueprint('departamento', __name__)

@departamento.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM departamento'))
        r = [row._asdict() for row in result.all()]
        return r

@departamento.get('/<string:departamento_cod>/')
def get_one(departamento_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM departamento WHERE cod='{departamento_cod}'"))
        r = result.first()._asdict()
        return r

@departamento.put('/<string:departamento_cod>/')
def put_one(departamento_cod):
    nome = request.get_json()['nome']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE departamento SET nome='{nome}' WHERE cod='{departamento_cod}'"
        ))
        connection.commit()
        return 'Ok'

@departamento.delete('/<string:departamento_cod>/')
def delete_one(departamento_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM departamento WHERE cod='{departamento_cod}'"
        ))
        connection.commit()
        return 'Ok'

@departamento.post('/')
def post_one():
    nome = request.get_json()['nome']
    cod = request.get_json()['cod']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"""INSERT INTO departamento (cod,nome) VALUES (
                {cod},
                '{nome}'
            )"""
        ))
        connection.commit()
        return 'Ok'
