# MINI PROJETO - Análise de Dados com Python
# Aluna: Irina Aleksiutina
# Turma: Analise_de_Dados_T1

import pandas as pd

# 1) Importação dos dados
# Importando o arquivo CSV com dados de vendas
# sep=';' porque o arquivo usa ponto e vírgula como separador
# encoding='latin1' para ler caracteres portugueses
df = pd.read_csv('Base Varejo.csv', sep=';', encoding='latin1')

# Mostrando informações básicas da base
print("INFORMAÇÕES BÁSICAS")
print(f"Número de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")
print("\nColunas e tipos de dados:")
print(df.dtypes)
print("\nPrimeiras 5 linhas:")
print(df.head())

