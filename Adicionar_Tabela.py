import sqlite3

cont = sqlite3.connect('clientes.db')
cursor = cont.cursor()

# Adicionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

cont.commit()
print('Novo campo adicionado com sucesso.')
cont.close()