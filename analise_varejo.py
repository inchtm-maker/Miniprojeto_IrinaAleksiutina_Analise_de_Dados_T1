# -------------------------------------------
# MINI PROJETO - Análise de Dados com Python
# Aluna: Irina Aleksiutina
# Turma: Analise_de_Dados_T1
# --------------------------------------------

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

# 2) Transformação de Strings, Integer e Float e Datetime
# Limpando espaços e padronizando texto em maiúsculas
df['CL_GENERO'] = df['CL_GENERO'].str.strip().str.upper()
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()
df['CL_SEG'] = df['CL_SEG'].str.strip().str.upper()
print("\nTRANSFORMAÇÃO DE DADOS")
print("Strings limpas!")

# Removendo colunas Float desnecessárias
df = df.loc[:, ~df.columns.str.contains('Unnamed')]
print(f"Colunas Float vazias removidas! Agora temos {df.shape[1]} colunas")

# Verificando tipos Integer
print(f"Tipos inteiros:")
print(f"CO_ID={df['CO_ID'].dtype}")
print(f"CL_ID={df['CL_ID'].dtype}")
print(f"CL_EC={df['CL_EC'].dtype}")
print(f"CL_FHL={df['CL_FHL'].dtype}")
print(f"PR_ID={df['PR_ID'].dtype}")

# Convertendo DATA de string para Datetime
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
print(f"DATA convertida para: {df['DATA'].dtype}")
print("\nTipos após transformação:")
print(df.dtypes)

print("\nPrimeiras 5 linhas:")
print(df.head())

