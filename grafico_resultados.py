import csv
import matplotlib.pyplot as plt

# Lê os dados do CSV
operacoes = []
tempos = []

with open('results.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pula o cabeçalho
    for row in reader:
        operacoes.append(row[0])
        tempos.append(float(row[1]))

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.bar(operacoes, tempos, color='royalblue')
plt.xlabel('Operações')
plt.ylabel('Tempo (s)')
plt.title('Benchmark de Desempenho no MySQL')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salva como imagem e exibe
plt.savefig('grafico_benchmark.png')
plt.show()
