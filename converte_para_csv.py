import pandas as pd
import numpy as np

copie_aqui_seu_dicionario = {
'ID_Imovel': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
'Tipo': ['Apartamento', 'Casa', 'Apartamento', 'Cobertura', 'Casa', 'Apartamento', 'Apartamento', 'Casa', 'Cobertura', 'Apartamento'],
'Bairro': ['Pinheiros', 'Moema', 'Itaim Bibi', 'Pinheiros', 'Vila Madalena', 'Itaim Bibi', 'Moema', 'Pinheiros', 'Vila Madalena', 'Itaim Bibi'],
'Quartos': [2, 4, 3, 3, 5, 1, 2, 3, 4, 2],
'Banheiros': [2, 3, 3, 4, 4, 1, 2, 2, 5, 2],
'Vagas': [1, 3, 2, 3, 4, 0, 2, 2, np.nan, 2],
'Área': [70, 200, 120, 180, 350, 45, 85, 150, 300, 95],
'Valor': [950000, 2800000, 2100000, 2500000, 4200000, 600000, 1100000, 1900000, 5100000, 1350000],
'Status': ['Disponível', 'Vendido', 'Disponível', 'Disponível', 'Vendido', 'Disponível', 'Disponível', 'Disponível', 'Vendido', 'Disponível']
}

df = pd.DataFrame(copie_aqui_seu_dicionario)
df.to_csv("dados/imoveis.csv", index=False)