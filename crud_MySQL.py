# CRUD utilizando Banco de dados MySQL

import mysql.connector

# CREATE
def create(nome, valor):
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome}", {valor})'
    cursor.execute(comando)
    conexao.commit() # Edita BD
    #resultado = cursor.fetchall() # Consulta BD

# READ
def read():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    #conexao.commit() # Edita BD
    resultado = cursor.fetchall() # Consulta BD
    print(resultado)

# UPDATE
def update(nome, valor):
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome}"'
    cursor.execute(comando)
    conexao.commit() # Edita BD
    #resultado = cursor.fetchall() # Consulta BD

# DELETE
def delete(nome):
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome}"'
    cursor.execute(comando)
    conexao.commit() # Edita BD
    #resultado = cursor.fetchall() # Consulta BD

if __name__ == '__main__':
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='hfbibru2286',
        database='bdyoutube'
    )
    cursor = conexao.cursor()

    # CRUD
    create('todynho', 3)
    create('chocolate', 15)
    read()
    update('todynho', 6)
    delete('todynho')

    cursor.close()
    conexao.close()
