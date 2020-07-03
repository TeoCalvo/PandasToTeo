import pandas as pd
import os

pd.set_option('display.max_columns', 5)

endereco_programa = os.path.join( os.path.abspath('.'), 'src')
endereco_programa = os.path.dirname( os.path.abspath(__file__) )

endereco_projeto = os.path.dirname( endereco_programa )
endereco_dados = os.path.join( endereco_projeto, 'data' )

filepath_csv = os.path.join( endereco_dados, 'tb_candidatura_2018.csv')
df_candidatura = pd.read_csv( filepath_csv, sep=";" )

df_candidatura.head()

# Combinando e modificando colunas

df_candidatura.columns

df_candidatura[['idade_data_eleicao', 'idade_data_posse']]
tipos_colunas = df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes
type( tipos_colunas )
print(tipos_colunas)

idades_velhas = ['idade_data_eleicao', 'idade_data_posse']
idades_nova = ['idade_eleicao', 'idade_posse']

# Aqui da pal!!! Tem dado faltandoooo
df_candidatura[idades_nova] = df_candidatura[idades_velhas].astype(int)
df_candidatura[idades_velhas].describe()

# Forma 1 de remover faltantes
del df_candidatura['idade_data_eleicao']

# Forma 2 de remover faltantes
df_candidatura_novo = df_candidatura.dropna(how='all', axis=1).copy() # retorna dataframe novo!!!
df_candidatura_novo.head()

df_candidatura_novo.columns

df_candidatura_novo['idade_data_posse'] = df_candidatura_novo['idade_data_posse'].astype(int)