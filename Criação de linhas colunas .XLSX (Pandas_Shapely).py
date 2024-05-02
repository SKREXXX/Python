import pandas as pd
from shapely.geometry import Point

# Ler o arquivo Excel
df = pd.read_excel('Arquivos.xlsx')

# Criar uma lista de pontos
pontos = []
for idx, row in df.iterrows():
    ponto = Point(row['x'], row['y'])
    pontos.append(ponto)

# Exibir os pontos
for idx, ponto in enumerate(pontos, start=1):
    print(f'Ponto {idx}: {ponto}')
