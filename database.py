import sqlite3

def create_table():
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            codigo INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            valor_unitario REAL NOT NULL,
            qtde_estoque INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_produto(codigo, nome, valor_unitario, qtde_estoque):
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO produtos (codigo, nome, valor_unitario, qtde_estoque) 
        VALUES (?, ?, ?, ?)
    ''', (codigo, nome, valor_unitario, qtde_estoque))
    conn.commit()
    conn.close()

def get_produtos():
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM produtos')
    produtos = c.fetchall()
    conn.close()
    return produtos

def update_produto(codigo, nome, valor_unitario, qtde_estoque):
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute('''
        UPDATE produtos 
        SET nome = ?, valor_unitario = ?, qtde_estoque = ?
        WHERE codigo = ?
    ''', (nome, valor_unitario, qtde_estoque, codigo))
    conn.commit()
    conn.close()

def delete_produto(codigo):
    conn = sqlite3.connect('produtos.db')
    c = conn.cursor()
    c.execute('DELETE FROM produtos WHERE codigo = ?', (codigo,))
    conn.commit()
    conn.close()
