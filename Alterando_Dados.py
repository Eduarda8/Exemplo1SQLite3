import sqlite3

cont = sqlite3.connect('clientes.db')
cursor = cont.cursor()

suap = "201610040081"
senha = "1234567"

# Alterando os dados da tabela;
cursor.execute("""
UPDATE clientes
SET suap = ?
WHERE senha = ?
""", (suap, senha))

cont.commit()
print('Dados atualizados com sucesso.')
cont.close()