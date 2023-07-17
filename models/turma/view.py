import random

from flask import Blueprint, current_app, request
from sqlalchemy.sql import text

turma = Blueprint('turma', __name__)

@turma.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM turma'))
        r = [row._asdict() for row in result.all()]
        return r

@turma.get('/<string:turma_cod>/')
def get_one(turma_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM turma WHERE id='{turma_cod}'"))
        r = result.first()._asdict()
        return r

@turma.put('/<string:turma_cod>/')
def put_one(turma_cod):
    vagas_ocupadas = request.get_json()['vagas_ocupadas']
    local = request.get_json()['local']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE turma SET vagas_ocupadas={vagas_ocupadas}, local='{local}' WHERE id='{turma_cod}'"
        ))
        connection.commit()
        return 'Ok'

@turma.delete('/<string:turma_cod>/')
def delete_one(turma_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM turma WHERE id='{turma_cod}'"
        ))
        connection.commit()
        return 'Ok'

@turma.post('/')
def post_one():
    id = random.randint(0,999)
    periodo = request.get_json()['periodo']
    professor_nome = request.get_json()['professor_nome']
    horario = request.get_json()['horario']
    vagas_ocupadas = request.get_json()['vagas_ocupadas']
    total_vagas = request.get_json()['total_vagas']
    local = request.get_json()['local']
    cod_disciplina = request.get_json()['cod_disciplina']
    cod_dpto = request.get_json()['cod_dpto']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"""INSERT INTO turma (id,periodo,professor_nome,horario,vagas_ocupadas,total_vagas,local,cod_disciplina,cod_dpto) VALUES (
                {id},
                '{periodo}',
                '{professor_nome}',
                '{horario}',
                {vagas_ocupadas},
                {total_vagas},
                '{local}',
                '{cod_disciplina}',
                {cod_dpto}
            )"""
        ))
        connection.commit()
        return 'Ok'
