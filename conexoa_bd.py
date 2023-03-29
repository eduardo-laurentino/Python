import mysql.connector
from mysql.connector import Error

conexao = mysql.connector.connect(
host = 'localhost',
database = 'nome do seu banco de dados',
user = 'seu usuário',
password = 'sua senha'
)

if conexao.is_connected():
    print('conexão bem sucedida')

insere = """insert into usuario (nome, senha) values ('Eduardo', 'password')"""
cursor = conexao.cursor()
cursor.execute(insere)
print("Dados inseridos com sucesso")


# Busca registros no banco de dados
busca = """select * from usuario"""
cursor = conexao.cursor()
cursor.execute(busca)
linhas = cursor.fetchall()
print(cursor.rowcount, "Registro(s) na tabela")
print(linhas)


apaga = """delete from usuario where nome = 'Eduardo'"""
cursor = conexao.cursor()
cursor.execute(apaga)
conexao.commit()