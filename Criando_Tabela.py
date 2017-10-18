# Sintaxe para conectar com o Banco de Dados;

import sqlite3

cont = sqlite3.connect('clientes.db')
# Informando o cursor;
cursor = cont.cursor()

# Criando a Tabela;
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
""")

print("Criado uma nova Tabela")
cont.close()