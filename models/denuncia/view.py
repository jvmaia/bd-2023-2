import random

from flask import Blueprint, current_app, request
from sqlalchemy.sql import text

denuncia = Blueprint('denuncia', __name__)

@denuncia.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM denuncia'))
        r = [row._asdict() for row in result.all()]
        return r

@denuncia.get('/<string:denuncia_cod>/')
def get_one(denuncia_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM denuncia WHERE id='{denuncia_cod}'"))
        r = result.first()._asdict()
        return r

@denuncia.put('/<string:denuncia_cod>/')
def put_one(denuncia_cod):
    denuncia = request.get_json()['denuncia']
    avaliacao = request.get_json()['avaliacao']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE denuncia SET denuncia='{denuncia}', avaliacao='{avaliacao}' WHERE id='{denuncia_cod}'"
        ))
        connection.commit()
        return 'Ok'

@denuncia.delete('/<string:denuncia_cod>/')
def delete_one(denuncia_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM denuncia WHERE id='{denuncia_cod}'"
        ))
        connection.commit()
        return 'Ok'

@denuncia.post('/')
def post_one():
    id = random.randint(0,9990)
    denuncia = request.get_json()['denuncia']
    avaliacao = request.get_json()['avaliacao']
    cod_estudante = request.get_json()['cod_estudante']
    cod_avaliador = request.get_json()['cod_avaliador']
    cod_avaliacao = request.get_json()['cod_avaliacao']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"""INSERT INTO denuncia (id,denuncia,avaliacao,cod_estudante,cod_avaliador,cod_avaliacao) VALUES (
                {id},
                '{denuncia}',
                '{avaliacao}',
                '{cod_estudante}',
                '{cod_avaliador}',
                {cod_avaliacao}
            )"""
        ))
        connection.commit()
        return 'Ok'
