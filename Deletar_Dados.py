import sqlite3

cont = sqlite3.connect('clientes.db')
cursor = cont.cursor()

senha = "uuuuu"

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE senha = ?
""", (senha,))

cont.commit()
print('Registro excluido com sucesso.')
cont.close()