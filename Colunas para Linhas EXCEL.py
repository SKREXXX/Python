import pandas as pd

# Ler o arquivo Excel
df = pd.read_excel('Arquivo.xlsx')

# Transformar colunas em linhas
df_transposto = df.T

# Arquivo Excel
df_transposto.to_excel('dados_transpostos.xlsx', header=False)

print("Arquivo Excel criado com sucesso: dados_transpostos.xlsx")
