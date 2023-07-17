from flask import Blueprint, current_app, request
from sqlalchemy.sql import text

disciplina = Blueprint('disciplina', __name__)

@disciplina.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM disciplina'))
        r = [row._asdict() for row in result.all()]
        return r

@disciplina.get('/<string:disciplina_cod>/')
def get_one(disciplina_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM disciplina WHERE cod='{disciplina_cod}'"))
        r = result.first()._asdict()
        return r

@disciplina.put('/<string:disciplina_cod>/')
def put_one(disciplina_cod):
    nome = request.get_json()['nome']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE disciplina SET nome='{nome}' WHERE cod='{disciplina_cod}'"
        ))
        connection.commit()
        return 'Ok'
    
@disciplina.delete('/<string:disciplina_cod>/')
def delete_one(disciplina_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM disciplina WHERE cod='{disciplina_cod}'"
        ))
        connection.commit()
        return 'Ok'

@disciplina.post('/')
def post_one():
    nome = request.get_json()['nome']
    cod = request.get_json()['cod']
    cod_dpto = request.get_json()['cod_dpto']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"INSERT INTO disciplina (nome,cod,cod_dpto) VALUES ('{nome}','{cod}','{cod_dpto}')"
        ))
        connection.commit()
        return 'Ok'
