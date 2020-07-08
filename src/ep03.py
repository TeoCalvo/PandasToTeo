import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', 10)

endereco_programa = os.path.join( os.path.abspath('.'), 'src')
endereco_programa = os.path.dirname( os.path.abspath(__file__) )

endereco_projeto = os.path.dirname( endereco_programa )
endereco_dados = os.path.join( endereco_projeto, 'data' )

filepath_csv = os.path.join( endereco_dados, 'tb_candidatura_2018.csv')
df_candidatura = pd.read_csv( filepath_csv, sep=";" )

df_candidatura.head()

### AULA DE HOJE É SOBRE LIMPEZA E FILTROS DE DADOS

# Identificando % de missings em cada coluna
df_candidatura.isna().sum() / df_candidatura.shape[0]

# Removendo colunas com apenas missings (NaNs)
df_candidatura = df_candidatura.dropna( how='all', axis=1)
df_candidatura.dropna(how="all", axis=1, inplace=True)

# Removendo candidatos que nao tem email ou composição legenda
df_candidatura.dropna( axis=0,
                       how='any',
                       subset=['composicao_legenda', 'email'],
                       inplace=True )

### VAMOS FILTRAR ESSA FITA!!!

df_candidatura['descricao_cargo'].unique()

df_candidatura['descricao_cargo'].nunique()

df_presidente_pstu = df_candidatura[ (df_candidatura['descricao_cargo'] == 'PRESIDENTE') &
                                     (df_candidatura['sigla_partido'] == 'PSTU') ]

# Pengando todos candidatos à presidência
df_presidente = df_candidatura[ (df_candidatura['descricao_cargo'] == 'PRESIDENTE') ].copy()

colunas_interesse = ['ano_eleicao',
                     'numero_turno',
                     'cpf',
                     'data_nascimento',
                     'descricao_cor_raca',
                     'descricao_estado_civil',
                     'descricao_genero',
                     'descricao_grau_instrucao',
                     'descricao_ocupacao',
                     'email',
                     'nome',
                     'nome_social',
                     'sigla_uf_nascimento',
                     'nome_partido',
                     'sigla_partido',
                     'descricao_cargo',
                     'descricao_situacao_candidatura' ]

df_presidente = df_presidente[colunas_interesse]

# Quantos cansidatos a presidente temos??
df_presidente.shape # 16

# Tem boi na linha amiguinhooo
df_presidente['cpf'].nunique()

df_presidente = ( df_presidente
                  .sort_values(by=['cpf','numero_turno'])
                  .drop_duplicates(subset=['cpf'], keep='first') )

df_presidente = df_presidente.where( df_presidente['descricao_situacao_candidatura'] == "APTO" ).dropna(how='all') # faz a mesma coisa que a linha de baixo
df_presidente = df_presidente[ df_presidente['descricao_situacao_candidatura'] == "APTO" ].copy() # Faz a mesma coisa que a linha de cima

df_presidente[['nome']]