import pandas as pd
import mysql.connector
import time
import csv

# Ler o CSV
df = pd.read_csv(r'datasets\olist_orders_dataset.csv')

# Conectar ao MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='null',
    database='projetodb'
)

cursor = conexao.cursor()


# Medir tempo de execução
# inicio = time.time()

# Inserir dados
# for _, row in df.iterrows():
#     cursor.execute(
#         """INSERT INTO orders (
#             order_id,
#             customer_id,
#             order_status,
#             order_purchase_timestamp,
#             order_approved_at,
#             order_delivered_carrier_date,
#             order_delivered_customer_date,
#             order_estimated_delivery_date
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
#         tuple(row)
#     )

# conexao.commit()
# fim = time.time()
# tempo_insercao_orders = fim - inicio

# for _, row in df.iterrows():
#     cursor.execute(
#         """INSERT INTO orders (
#             order_id,
#             customer_id,
#             order_Status,
#             order_purchase_timestamp,
#             order_approved_at,
#             order_delivered_carrier_date,
#             order_delivered_customer_date,
#             order_estimated_delivery_date
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
#         tuple(row)
#     )

# def consulta_simples():
#     inicio = time.time()
#     cursor.execute("SELECT * FROM customers WHERE customer_city = 'Governador Valadares'")
#     resultado = cursor.fetchall()
#     fim = time.time()
#     return fim - inicio

# tempo_consulta = consulta_simples()

# def consulta_complexa():
#     inicio = time.time()
#     cursor.execute("SELECT c.customer_state AS Estados, COUNT(o.order_id) AS total_pedidos " \
# "FROM customers c " \
# "JOIN orders o ON c.customer_id = o.customer_id " \
# "GROUP BY c.customer_state " \
# "HAVING total_pedidos > 50 " \
# "ORDER BY total_pedidos DESC")
#     resultado = cursor.fetchall()
#     fim = time.time()
#     return fim - inicio

# tempo_consulta = consulta_complexa()

# def atualizar():
#     inicio = time.time()
#     cursor.execute("UPDATE customers " \
# "SET customer_city = 'Uai sô '" \
# "WHERE customer_state = 'MG'")
#     conexao.commit()
#     fim = time.time()
#     return fim - inicio

# tempo_consulta = atualizar()

def deletar():
    inicio = time.time()
    cursor.execute("DELETE FROM customers WHERE customer_state = 'ES'")
    conexao.commit()
    fim = time.time()
    return fim - inicio

tempo_consulta = deletar()

# Salvar o resultado no CSV
def salvar_resultados_csv(linha_resultado):
    with open('results.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Operação', 'Tempo (s)'])
        writer.writerow(linha_resultado)

operacao = 'Exclusão em massa'
linha_resultado = [operacao, round(tempo_consulta, 4)]

print(f"Tempo total da exclusão: {tempo_consulta:.4f} segundos")

salvar_resultados_csv(linha_resultado)

cursor.close()
conexao.close()
