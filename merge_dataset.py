import pandas as pd



arquivo_1 = input('Entre com o nome do primeiro arquivo')
arquivo_2 = input("Entre com o nome do segundo arquivo")
arquiv_gerado = input("Nome do arquivo a ser gerado")

data_1 = pd.read_excel(arquivo_1)
data_2 = pd.read_excel(arquivo_2)

data_merged = pd.concat([data_1,data_2],axis=0)

data_merged.to_excel(arquiv_gerado)
