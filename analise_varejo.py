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
print("1) INFORMAÇÕES BÁSICAS")
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
print("\n2) TRANSFORMAÇÃO DE DADOS")
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

# 3) Limpeza de Nulos e Duplicatas
print("\n3)LIMPEZA DE DADOS")

# Verificando valores nulos por coluna
print("Valores nulos por coluna:")
print(df.isnull().sum())

# Verificando duplicatas
print(f"\nNúmero de duplicatas: {df.duplicated().sum()}")

# Verificando valores únicos
print("\nValores únicos de CO_ID:")
print(df['CO_ID'].unique())

print("\nValores únicos de CL_ID:")
print(df['CL_ID'].unique())

print("\nValores únicos de CL_GENERO:")
print(df['CL_GENERO'].unique())

print("\nValores únicos de CL_EC:")
print(df['CL_EC'].unique())

print("\nValores únicos de CL_FHL:")
print(df['CL_FHL'].unique())

print("\nValores únicos de CL_SEG:")
print(df['CL_SEG'].unique())

print("\nValores únicos de PR_ID:")
print(df['PR_ID'].unique())

print("\nValores únicos de PR_CAT:")
print(df['PR_CAT'].unique())

print("\nValores únicos de PR_NOME:")
print(df['PR_NOME'].unique())

# Corrigindo categoria inválida #N/D
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'Sem Categoria')
print("\nCategoria #N/D substituída por 'Sem Categoria'!")

# Removendo duplicatas
duplicatas = df.duplicated().sum()
df = df.drop_duplicates()
print(f"Duplicatas removidas: {duplicatas}")
print(f"Registros após limpeza: {df.shape[0]}")

# 4) Estatística Descritiva
# Calculando estatísticas da coluna CL_FHL (Número de filhos)
print("\n4) ESTATÍSTICA DESCRITIVA")
print("Estatísticas da coluna CL_FHL (Número de filhos):\n")

print(f"Média:          {df['CL_FHL'].mean():.2f}")
print(f"Mediana:        {df['CL_FHL'].median():.2f}")
print(f"Desvio padrão:  {df['CL_FHL'].std():.2f}")
print(f"Moda:           {df['CL_FHL'].mode()[0]:.2f}")
print(f"Máximo:         {df['CL_FHL'].max():.2f}")
print(f"Mínimo:         {df['CL_FHL'].min():.2f}")
print(f"Contagem:       {df['CL_FHL'].count()}")
print(f"\nQuartis:")
print(df['CL_FHL'].quantile([0.25, 0.50, 0.75]))

# 5) Relatório e Documentação
print("\n5) RELATÓRIO FINAL")

# Agrupamento 1: Total de compras por Gênero
print("1. Total de compras por Gênero:")
print(df.groupby('CL_GENERO')['CO_ID'].count())

# Agrupamento 2: Total de compras por Categoria
print("\n2. Total de compras por Categoria:")
print(df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False))

# Conclusões finais
print("\nCONCLUSÕES")
print("1. A base contém 830.000 registros com 14 colunas")
print("2. Foram removidas 96.553 duplicatas")
print("3. A maioria dos clientes não tem filhos (moda = 0)")
print("4. Mulheres compram mais que homens (382k vs 351k)")
print("5. Alimentos é a categoria mais vendida")
print("6. 75% dos clientes têm menos de 2 filhos")

# 6) Salvando dataframe limpo
df.to_csv('df_limpo.csv', index=False)
print("\nArquivo df_limpo.csv salvo com sucesso!")