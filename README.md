# Benchmark MySQL – Desempenho de Operações

Este projeto tem como objetivo realizar uma análise comparativa de desempenho no banco de dados MySQL, executando operações típicas como inserção em massa, consultas simples e complexas, atualização e deleção.

## 📁 Estrutura

- `benchmark_mysql.py`: script principal com inserções, consultas e medições de tempo.
- `grafico_resultados.py`: gera gráfico com base no `results.csv`.
- `results.csv`: tempos de execução registrados.
- `grafico_benchmark.png`: imagem com gráfico de desempenho.
- `dataset/dataset_exemplo.csv`: simulação de dados usados na inserção.
- `Capa_Relatorio_Benchmark.docx`: capa do relatório técnico.

## 🚀 Como rodar

1. Instale as dependências:
   ```
   pip install mysql-connector-python matplotlib
   ```

2. Execute o benchmark:
   ```
   python benchmark_mysql.py
   ```

3. Gere o gráfico:
   ```
   python grafico_resultados.py
   ```

## 📊 Dataset

[Download do dataset de exemplo](dataset/dataset_exemplo.csv)

## 👨‍🏫 Professor

Prof. Alexandre Barbosa de Souza  
Curso de Sistemas de Informações (UniSales)

---

Ramon Bischoli Kuster – 2025
