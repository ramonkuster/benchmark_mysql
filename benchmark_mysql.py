import mysql.connector
import time
import csv
import random

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ramon@2002',
    database='benchmark'
)
cursor = conn.cursor()

# Inserção de clientes
def inserir_clientes(n):
    inicio = time.time()
    for i in range(n):
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)",
                       (f'Cliente{i}', f'cliente{i}@email.com'))
    conn.commit()
    fim = time.time()
    return fim - inicio

# Inserção de produtos
def inserir_produtos(n):
    inicio = time.time()
    for i in range(n):
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)",
                       (f'Produto{i}', round(random.uniform(10.0, 100.0), 2)))
    conn.commit()
    fim = time.time()
    return fim - inicio

# Consulta simples
def consulta_simples():
    inicio = time.time()
    cursor.execute("SELECT * FROM produtos WHERE preco > 50")
    resultado = cursor.fetchall()
    fim = time.time()
    return fim - inicio

# Consulta complexa
def consulta_complexa():
    inicio = time.time()
    cursor.execute("""
        SELECT p.id, c.nome, pr.nome, ip.quantidade 
        FROM pedidos p 
        JOIN clientes c ON p.cliente_id = c.id
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN produtos pr ON ip.produto_id = pr.id
    """)
    resultado = cursor.fetchall()
    fim = time.time()
    return fim - inicio

# Atualização de produtos
def atualizar_produtos():
    inicio = time.time()
    cursor.execute("""
        UPDATE produtos
        SET preco = preco * 1.10
        WHERE preco < 50
    """)
    conn.commit()
    fim = time.time()
    return fim - inicio

# Exclusão de clientes
def deletar_clientes():
    inicio = time.time()
    cursor.execute("""
        DELETE FROM clientes
        WHERE nome LIKE 'Cliente9%'
    """)
    conn.commit()
    fim = time.time()
    return fim - inicio

# Salvando os resultados em CSV
def salvar_resultados_csv(resultados):
    with open('results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Operação', 'Tempo (s)'])
        writer.writerows(resultados)

# Executando tudo
resultados = []
resultados.append(['Inserção de Clientes', inserir_clientes(1000)])
resultados.append(['Inserção de Produtos', inserir_produtos(1000)])
resultados.append(['Consulta Simples', consulta_simples()])
resultados.append(['Consulta Complexa', consulta_complexa()])
resultados.append(['Atualização em Massa', atualizar_produtos()])
resultados.append(['Exclusão em Massa', deletar_clientes()])

salvar_resultados_csv(resultados)

# Fechando conexão
cursor.close()
conn.close()
