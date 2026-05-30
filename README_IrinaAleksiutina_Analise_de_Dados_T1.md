# MINI PROJETO - Análise de Dados com Python
Aluna: Irina Aleksiutina  
Turma: Analise_de_Dados_T1

## Como executar
1. Abra a pasta no VsCode
2. Instale o pandas: `pip install pandas`
3. Execute: `python3 analise_varejo.py`

## Estrutura do Projeto
- `analise_varejo.py` — script principal com toda a análise
- `Base Varejo.csv` — base de dados original
- `df_limpo.csv` — base de dados limpa

## O que foi feito
1) Carregamento e visualização dos dados
2) Transformação de tipos (strings, integers, datetime)
3) Limpeza de dados (duplicatas, categorias inválidas)
4) Estatística descritiva da coluna CL_FHL
5) Agrupamentos e relatório final
6) Salvamento do dataframe limpo

## Reflexão sobre ETL e Qualidade de Dados
ETL significa Extração, Transformação e Carga de dados.
Neste projeto aprendemos que dados reais sempre têm problemas:
- Colunas com tipos incorretos (DATA como string)
- Categorias inválidas (#N/D)
- Registros duplicados (96.553 duplicatas!)
A limpeza dos dados é essencial antes de qualquer análise.
Dados de qualidade geram insights confiáveis.

## Insights obtidos
1. A base original contém 830.000 registros com 14 colunas
2. Após limpeza: 733.447 registros com 10 colunas
3. Foram removidas 96.553 duplicatas
4. A maioria dos clientes não tem filhos (moda = 0)
5. Mulheres compram mais que homens (382k vs 351k)
6. Alimentos é a categoria mais vendida (384.197 compras)
7. 75% dos clientes têm menos de 2 filhos