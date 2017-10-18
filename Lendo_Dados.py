import sqlite3

cont = sqlite3.connect('usuarios.db')
cursor = cont.cursor()

# Lendo os dados;
cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)
cont.close()