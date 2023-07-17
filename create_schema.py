from app import db
from sqlalchemy.sql import text

with open('setup_bd.sql', 'r') as setup_sql_file:
    setup_sql = setup_sql_file.read()
    with db.engine.connect() as connection:
        connection.execute(text(setup_sql))
