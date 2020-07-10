import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', 10)
pd.set_option('display.precision', 4)

endereco_programa = os.path.join( os.path.abspath('.'), 'src')
endereco_programa = os.path.dirname( os.path.abspath(__file__) )

endereco_projeto = os.path.dirname( endereco_programa )
endereco_dados = os.path.join( endereco_projeto, 'data' )

filepath_csv = os.path.join( endereco_dados, 'tb_candidatura_2018.csv')
df_candidatura = pd.read_csv( filepath_csv, sep=";" )

# Objetivo da live: Encontrar a quantidade de deputados por estado, cor_raca, sexo, etc...

remove_columns = ['despesa_maxima_campanha', 'declara_bens', 'sigla_legenda', 'titulo_eleitoral' ]
keep_columns = list( set( df_candidatura.columns ) - set( remove_columns ) )

# Filtrando os candidatos a deputados estaduais
df_dept_estadual = df_candidatura[ (df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL') &
                                   (df_candidatura['descricao_situacao_candidatura'] == 'APTO') ][keep_columns]


# Percentual de aptos
df_dept_estadual.shape[0] / df_candidatura[ df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL'].shape[0]

df_dept_estadual.shape # Quantidade da nossa base...
df_dept_estadual['cpf'].nunique() # Sem duplicatas, bola para frente!!

# Isso é um DataFrame, pois estamos usando [['cpf']], mas ele é multiIndex ('sigla_uf', 'descricao_genero')
agrupa_estado_genero = df_dept_estadual.groupby( ['sigla_uf', 'descricao_genero'] )[['cpf']].nunique()

# Desempinha aos valores
df_estado_genero = agrupa_estado_genero.unstack()

# Remove multiIndex das colunas
df_estado_genero.columns = df_estado_genero.columns.droplevel()

# Reseta o índice do dataframe
df_estado_genero = df_estado_genero.reset_index()

# importando o patrimônio dos colarinhos brancos...

filepath_xlsx = os.path.join(endereco_dados, 'tb_declaracao_2018.xlsx')
df_patrimonio = pd.read_excel(filepath_xlsx)

# Agrupando para saber o patrimonio TOTAL dos camaradas...
df_patrimonio_candidato = (df_patrimonio.groupby( ['numero_sequencial'] )[['valor']]
                                        .sum()
                                        .reset_index())

# Megre de patrimonio
df_full = pd.merge( left = df_candidatura,
                    right = df_patrimonio_candidato,
                    how = 'left',
                    on = ['numero_sequencial'] )

# Descobrir partido com maior patrimomo medio entre os candidatos
df_filtrado = ( df_full[ df_full['descricao_situacao_candidatura']  == 'APTO' ]
                .sort_values( ['cpf','numero_turno'] )
                .drop_duplicates( "cpf", keep='first' )
                .fillna({"valor": 0}) )

# Descobrindo os partidos mais "ricos"
df_partido = df_filtrado.groupby( ["sigla_partido"] ).agg({"valor":['sum', 'mean', 'median']})
df_partido.sort_values( [('valor', 'median')], inplace=True )
print(df_partido)