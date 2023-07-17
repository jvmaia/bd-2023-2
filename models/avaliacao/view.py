import random

from flask import Blueprint, current_app, request
from sqlalchemy.sql import text

avaliacao = Blueprint('avaliacao', __name__)

@avaliacao.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM avaliacao'))
        r = [row._asdict() for row in result.all()]
        return r

@avaliacao.get('/<string:avaliacao_cod>/')
def get_one(avaliacao_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM avaliacao WHERE id='{avaliacao_cod}'"))
        r = result.first()._asdict()
        return r

@avaliacao.put('/<string:avaliacao_cod>/')
def put_one(avaliacao_cod):
    nota = request.get_json()['nota']
    avaliacao = request.get_json()['avaliacao']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE avaliacao SET nota={nota}, avaliacao='{avaliacao}' WHERE id='{avaliacao_cod}'"
        ))
        connection.commit()
        return 'Ok'

@avaliacao.delete('/<string:avaliacao_cod>/')
def delete_one(avaliacao_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM avaliacao WHERE id='{avaliacao_cod}'"
        ))
        connection.commit()
        return 'Ok'

@avaliacao.post('/')
def post_one():
    id = random.randint(0,9990)
    nota = request.get_json()['nota']
    avaliacao = request.get_json()['avaliacao']
    cod_estudante = request.get_json()['cod_estudante']
    cod_turma = request.get_json()['cod_turma']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"""INSERT INTO avaliacao (id,nota,avaliacao,cod_estudante,cod_turma) VALUES (
                {id},
                {nota},
                '{avaliacao}',
                '{cod_estudante}',
                '{cod_turma}'
            )"""
        ))
        connection.commit()
        return 'Ok'
