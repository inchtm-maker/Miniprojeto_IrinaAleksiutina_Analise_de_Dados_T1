# MINI PROJETO - Análise de Dados com Python
Aluna: Irina Aleksiutina  
Turma: Analise_de_Dados_T1

## Descrição do Projeto
Análise Exploratória de Dados aplicada a uma base de vendas 
de varejo com 830.000 registros reais de compras.

## Como executar
1. Abra a pasta no VsCode
2. Instale o pandas: `pip install pandas`
3. Execute: `python3 analise_varejo.py`

## Estrutura do Projeto
- `analise_varejo.py` — script principal com toda a análise
- `Base Varejo.csv` — base de dados original

## O que foi feito
1) Carregamento e visualização dos dados
2) Transformação de tipos (strings, integers, datetime)
3) Limpeza de dados (duplicatas, categorias inválidas)
4) Estatística descritiva da coluna CL_FHL
5) Agrupamentos e relatório final

## Insights obtidos
1. A base contém 830.000 registros com 14 colunas
2. Foram removidas 96.553 duplicatas
3. A maioria dos clientes não tem filhos (moda = 0)
4. Mulheres compram mais que homens (382k vs 351k)
5. Alimentos é a categoria mais vendida (384.197 compras)
6. 75% dos clientes têm menos de 2 filhos