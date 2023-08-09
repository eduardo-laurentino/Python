/* TABELA DE FUNÇÕES */

CREATE TABLE IF NOT EXISTS funcao (
  id int(11) NOT NULL AUTO_INCREMENT,
  cod varchar(5) NOT NULL,
  nome varchar(50) NOT NULL,
  PRIMARY KEY (id)
);


/* TABELA DE FUNCIONÁRIOS */
CREATE TABLE IF NOT EXISTS funcionarios (
  id int(11) NOT NULL AUTO_INCREMENT,
  cpf varchar(11) NOT NULL DEFAULT '',
  nome_funcionario varchar(50) NOT NULL,
  funcao_pessoa int(11) NOT NULL DEFAULT 0,
  salario float NOT NULL DEFAULT 0,
  telefone varchar (15) NOT NULL DEFAULT '',
  PRIMARY KEY (id),
  FOREIGN KEY (funcao_pessoa) REFERENCES funcao (id) 
);
