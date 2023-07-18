# Relatorio

### Aluno: 190110007

## Introducao
O objetivo desse trabalho é criar um sistema de CRUD para denúncias e avaliações de cada turma do semestre, dessa forma estão incluídos (alunos, professores, departamentos, turmas e disciplinas)

### Tecnologias utilizadas
- No frontend utilizei HTML e Javascript puros, por apresentar uma simplicidade e cumprir os requisitos do trabalho, sem necessidade de adicionarmos complexidade extra ao projeto
- No backend utilizei Python com Flask, por ter um maior conhecimento com a linguagem, para conexão com o banco de dados utilizei SQLAlchemy, onde o utilizei para rodar os SQLs do CRUD e executar nossa procedure.

## Diagrama
![diagrama (1)](https://github.com/jvmaia/bd-2023-2/assets/13905466/5afe530f-5ea0-4c61-8dc9-47ee5662b349)


## Avaliação das formas normais
Tabela "departamento":

A tabela possui uma única coluna, "cod", como chave primária.
Não há dependências funcionais adicionais presentes nessa tabela.
Portanto, a tabela "departamento" está na primeira forma normal (1NF).
Tabela "professor":

Tabela "professor":
A tabela possui as seguintes colunas: "nome" (chave primária), "cod" e "cod_departamento".
Não há dependências funcionais adicionais presentes nessa tabela.
Portanto, a tabela "professor" também está na primeira forma normal (1NF).
Tabela "disciplina":

Tabela "disciplina":
A tabela possui as seguintes colunas: "cod" (chave primária), "nome" e "cod_dpto".
Não há dependências funcionais adicionais presentes nessa tabela.
Portanto, a tabela "disciplina" também está na primeira forma normal (1NF).

## Scripts
- [Script para gerar o schema](setup_bd.sql)
- [Script para popular o banco](populate_bd.sql)

## Conclusão
Nesse trabalho consegui demonstrar que mesmo com as ferramentas simples (HTML e Javascript puros) conseguimos criar um sistema de cadastro funcional e que apresenta uma boa performance e é capaz de rodar até nos computadores mais simples, sem a necessidade do carregamento de libs pesadas e complexas.
