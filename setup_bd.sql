CREATE TABLE usuario (
    email TEXT,
    matricula TEXT,
    curso TEXT,
    nome TEXT,
    senha TEXT,
    eh_administrador BOOLEAN,
    foto BYTEA,
    PRIMARY KEY(matricula)
);
CREATE TABLE departamento (
    nome TEXT,
    cod INT,
    PRIMARY KEY(cod)
);
CREATE TABLE professor (
    nome TEXT,
    cod INT,
    cod_departamento INT,
    PRIMARY KEY(nome),
    CONSTRAINT fk_departamento
        FOREIGN KEY (cod_departamento)
            REFERENCES departamento(cod)
);
CREATE TABLE disciplina (
    nome TEXT,
    cod TEXT,
    cod_dpto INT,
    PRIMARY KEY(cod),
    CONSTRAINT fk_departamento
        FOREIGN KEY (cod_dpto)
            REFERENCES departamento(cod)
);

CREATE TABLE turma (
    id INT,
    periodo TEXT,
    professor_nome TEXT,
    horario TEXT,
    vagas_ocupadas INT,
    total_vagas INT,
    local TEXT,
    cod_disciplina TEXT,
    cod_dpto INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_departamento
        FOREIGN KEY (cod_dpto)
            REFERENCES departamento(cod),
    CONSTRAINT fk_disciplina
        FOREIGN KEY (cod_disciplina)
            REFERENCES disciplina(cod),
    CONSTRAINT fk_professor
        FOREIGN KEY (professor_nome)
            REFERENCES professor(nome)
);

CREATE TABLE avaliacao (
    id INT ,
    nota INT,
    avaliacao TEXT,
    cod_estudante TEXT,
    cod_turma INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_usuario
        FOREIGN KEY (cod_estudante)
            REFERENCES usuario(matricula),
    CONSTRAINT fk_turma
        FOREIGN KEY (cod_turma)
            REFERENCES turma(id)
);

CREATE TABLE denuncia (
    id INT ,
    denuncia TEXT,
    avaliacao TEXT,
    cod_estudante TEXT,
    cod_avaliador TEXT,
    cod_avaliacao INT ,
    PRIMARY KEY(id),
    CONSTRAINT fk_usuario
        FOREIGN KEY (cod_estudante)
            REFERENCES usuario(matricula),
    CONSTRAINT fk_avaliacao
        FOREIGN KEY (cod_avaliacao)
            REFERENCES avaliacao(id),
    CONSTRAINT fk_avaliador
        FOREIGN KEY (cod_avaliador)
            REFERENCES usuario(matricula)
);

create procedure sumir()
language plpgsql
as $$
begin
    DROP SCHEMA public CASCADE;
end;$$;


create view contagem_turmas AS select count(*) from turma;
