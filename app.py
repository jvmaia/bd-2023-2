import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask.cli import AppGroup
from sqlalchemy import text


app = Flask(__name__)
CORS(app)
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PW = os.environ['POSTGRES_PW']
POSTGRES_URL = os.environ['POSTGRES_URL']
POSTGRES_DATABASE = os.environ['POSTGRES_DATABASE']
DB_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DATABASE}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)
app.db = db

@app.route('/')
def hello_world():
    return 'Ok'

from models import disciplina
app.register_blueprint(
    disciplina.disciplina,
    url_prefix='/disciplinas'
)

from models import departamento
app.register_blueprint(
    departamento.departamento,
    url_prefix='/departamentos'
)

from models import turma
app.register_blueprint(
    turma.turma,
    url_prefix='/turmas'
)

from models import avaliacao
app.register_blueprint(
    avaliacao.avaliacao,
    url_prefix='/avaliacoes'
)

from models import denuncia
app.register_blueprint(
    denuncia.denuncia,
    url_prefix='/denuncias'
)

from models import professor
app.register_blueprint(
    professor.professor,
    url_prefix='/professores'
)

from models import usuario
app.register_blueprint(
    usuario.usuario,
    url_prefix='/usuarios'
)

cli = AppGroup()
@cli.command('setup_database')
def setup_db():
    print('Setting up database...')
    with open('setup_bd.sql', 'r') as setup_sql_file:
        setup_sql = setup_sql_file.read()
        print('sql readed')
        with db.engine.connect() as connection:
            print('connected to db', connection)
            result = connection.execute(text(setup_sql))
            print(f'{result}')
            connection.commit()

app.cli.add_command(setup_db)

@cli.command('populate_database')
def populate_db():
    print('Populating up database...')
    with open('populate_bd.sql', 'r') as populate_sql_file:
        populate_sql = populate_sql_file.read()
        print('sql readed')
        with db.engine.connect() as connection:
            print('connected to db', connection)
            result = connection.execute(text(populate_sql))
            print(f'{result}')
            connection.commit()

app.cli.add_command(populate_db)
