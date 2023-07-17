# PROJETO BANCO DE DADOS
## Aluno: 190110007

### Como rodar?
- clone o projeto e execute `docker-compose up --build`
- ao terminar de rodar o projeto será necessário executar os seguintes comandos para criar o schema e popular o banco de dados:
    -- `docker exec -it project_web_1 /bin/bash`
    -- `flask setup_database`
    -- `flask populate_database`
- assim, você já possui todos os dados que foram fornecidos nos CSVs para inserção no banco

