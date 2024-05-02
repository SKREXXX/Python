import pandas as pd
import xml.etree.ElementTree as ET

# Parsear o arquivo XML
tree = ET.parse(r'Arquivo.XML')
root = tree.getroot()

# Criar uma lista para armazenar os dados
data = []

# Iterar sobre os elementos do XML e extrair os dados
for child in root:
    data.append({
        'Coluna1': child.find('-').text,
        'Coluna2': child.find('-').text
    })

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

print(df)
