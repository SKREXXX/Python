import pandas as pd

# Ler o arquivo .dat e criar um DataFrame
with open('arquivos.dat', 'r') as file:
    lines = file.readlines()

# Dividir os dados em três colunas
data = [line.strip().split() for line in lines]
df = pd.DataFrame(data, columns=['Date 01', 'Date 02', 'Variação'])

# Salvar os dados em um arquivo Excel
df.to_excel('arquivos.xlsx', index=False)

print("Arquivo Excel criado com sucesso: arquivos.xlsx")
