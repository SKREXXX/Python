import pandas as pd

input_file = 'arquivos.kml'

output_file = 'arquivos.csv'

df = pd.read_html(input_file)[0]

csv_data = df.to_csv(sep=';', index=False)

csv_data = csv_data.replace(';', ',')

with open(output_file, 'w') as file:
    file.write(csv_data)