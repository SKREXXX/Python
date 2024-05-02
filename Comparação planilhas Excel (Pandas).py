import pandas as pd

# Caminhos para os arquivos Excel
caminho_arquivo1 = 'C:/Users/Natan/Desktop/ARQUIVOS/Trabalhadas/Bacia (Colunas).xlsx'
caminho_arquivo2 = 'C:/Users/Natan/Desktop/ARQUIVOS/Trabalhadas/p240222a010322.xlsx'

# Ler os arquivos Excel em DataFrames
df1 = pd.read_excel(caminho_arquivo1, sheet_name='Sheet1', na_values=['NA'])
df2 = pd.read_excel(caminho_arquivo2, sheet_name='Sheet1', na_values=['NA'])

# Comparar as colunas 'coluna1' de cada DataFrame
comparacao = df1['Coluna1'].equals(df2['Coluna1'])

# Exibir o resultado da comparação
if comparacao:
    print("As colunas 'coluna1' são iguais nos dois arquivos.")
else:
    print("As colunas 'coluna1' são diferentes nos dois arquivos.")
