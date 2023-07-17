import base64

from flask import Blueprint, current_app, request
from sqlalchemy.sql import text
from sqlalchemy.types import LargeBinary, String
from sqlalchemy import bindparam

usuario = Blueprint('usuario', __name__)

@usuario.get('/')
def get():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text('SELECT email,matricula,curso,nome,foto FROM usuario'))
        r = [{**row._asdict(), "foto":base64.encodebytes(row._asdict()['foto'].tobytes()).decode() } for row in result.all()]
        return r

@usuario.post('/login')
def post():
    matricula = request.get_json()['matricula']
    senha = request.get_json()['senha']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT eh_administrador FROM usuario where matricula='{matricula}' and senha='{senha}'"))
        r = result.first()
        return { 'success': r != None, 'administrador':  r._asdict().get('eh_administrador') if (r != None)  else False}

@usuario.get('/<string:usuario_cod>/')
def get_one(usuario_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(f"SELECT email,matricula,curso,nome FROM usuario WHERE matricula='{usuario_cod}'"))
        r = result.first()._asdict()
        return r

@usuario.put('/<string:usuario_cod>/')
def put_one(usuario_cod):
    nome = request.get_json()['nome']
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"UPDATE usuario SET nome='{nome}' WHERE matricula='{usuario_cod}'"
        ))
        connection.commit()
        return 'Ok'
    
@usuario.delete('/<string:usuario_cod>/')
def delete_one(usuario_cod):
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"DELETE FROM usuario WHERE matricula='{usuario_cod}'"
        ))
        connection.commit()
        return 'Ok'


@usuario.get('/sumir/')
def delete_everything():
    with current_app.db.engine.connect() as connection:
        result = connection.execute(text(
            f"CALL sumir()"
        ))
        connection.commit()
        return 'Ok'

@usuario.post('/')
def post_one():
    data = request.form.to_dict()
    print(data)
    nome = data['nome']
    email = data['email']
    matricula = data['matricula']
    curso = data['curso']
    senha = data['senha']
    eh_administrador = data['eh_administrador']
    foto = request.files['foto'].read()
    with current_app.db.engine.connect() as connection:
        stmt = text(
            f"""INSERT INTO usuario (email,matricula,curso,nome,senha,eh_administrador,foto) VALUES (
                '{email}',
                '{matricula}',
                '{curso}',
                '{nome}',
                '{senha}',
                {eh_administrador},
                :X ::bytea
            )"""
        ).bindparams(bindparam('X',type_=LargeBinary))

        result = connection.execute(stmt, {'X': foto})
        connection.commit()
        return 'Ok'
