import random

from flask import Blueprint, current_app, request
from sqlalchemy.sql import text

professor = Blueprint('professor', __name__)

@professor.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM professor'))
        r = [row._asdict() for row in result.all()]
        return r

@professor.get('/<string:professor_cod>/')
def get_one(professor_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM professor WHERE cod='{professor_cod}'"))
        r = result.first()._asdict()
        return r

@professor.put('/<string:professor_cod>/')
def put_one(professor_cod):
    nome = request.get_json()['nome']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE professor SET nome='{nome}' WHERE cod='{professor_cod}'"
        ))
        connection.commit()
        return 'Ok'

@professor.delete('/<string:professor_cod>/')
def delete_one(professor_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM professor WHERE cod='{professor_cod}'"
        ))
        connection.commit()
        return 'Ok'

@professor.post('/')
def post_one():
    nome = request.get_json()['nome']
    cod = random.randint(0,99999)
    cod_departamento = request.get_json()['cod_departamento']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"""INSERT INTO professor (cod,nome,cod_departamento) VALUES (
                {cod},
                '{nome}',
                '{cod_departamento}'
            )"""
        ))
        connection.commit()
        return 'Ok'
