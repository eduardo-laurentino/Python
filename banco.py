import pymysql.cursors

connection = pymysql.connect(host='localhost', 
                                user='root', 
                                password='',
                                database='banco_Poo', 
                                charset='utf8mb4', 
                                cursorclass=pymysql.cursors.DictCursor) 


with connection.cursor() as c:
    sql = "SELECT * FROM conta_corrente"
    c.execute(sql)
    resultado = c.fetchall() 
    print(resultado)
    print("\n\n")
    sql = "SELECT nome, numero, agencia, saldo from conta_corrente join clientes on conta_corrente.titular = clientes.id;"
    c.execute(sql)
    resultado = c.fetchall()
    print(resultado)
    


    print("\n\n")
    sql = "DELETE FROM conta_corrente WHERE id = '4'"
    c.execute(sql)
    resultado = c.fetchall()

# Cadastrando Cliente
with connection.cursor() as c:
    sql = "INSERT INTO clientes (nome, cpf) VALUES (%s, %s)"
    c.execute(sql, ('Ana Paula', '07576456'))


#cadastrando Conta
with connection.cursor() as c:
    sql = "INSERT INTO conta_corrente (titular, numero, agencia, saldo) VALUES (%s, %s, %s, %s)"
    c.execute(sql, ('3', '20072', '2412', '1500.00'))



with connection.cursor() as cursor:
    sql = "UPDATE clientes SET nome=%s WHERE id=%s"
    cursor.execute(sql, ('Ana Maria Gomes', 3))


    connection.commit()
    connection.close()