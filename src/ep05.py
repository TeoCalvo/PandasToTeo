import pandas as pd
import os
import sqlalchemy
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--cargo", '-c', help='Nome do cargo', type=str)
parser.add_argument("--numero", '-n', help='Quantidade de tops', type=int)
args = parser.parse_args()

SRC_DIR = os.path.join( os.path.abspath('.'), 'src' ) # Diretório de código
SRC_DIR = os.path.dirname( os.path.abspath(__file__) ) # Diretório de código
BASE_DIR = os.path.dirname( SRC_DIR ) # Diretório do projeto
DATA_DIR = os.path.join( BASE_DIR, 'data' ) # Diretório dos dados

def import_query(path:str, **kwargs ):
    '''Função para importar uma query de uma diretório..'''
    with open( path, 'r', **kwargs ) as file_open:
        query = file_open.read()
    return query

# Esse carai é a conexão!!!
con = sqlalchemy.create_engine( "sqlite:///" + os.path.join( DATA_DIR, 'brasilio.db' )  )
con.table_names()

df_candidatos = pd.read_sql_table('tb_candidatura', con)

query_candidatos = import_query( os.path.join(SRC_DIR, 'candidatos.sql') )
query_candidatos = query_candidatos.format(cargo='SUPLENTE',
                                           status_candidatura='APTO')

df_candidatos_2 = pd.read_sql_query( query_candidatos, con )
print(df_candidatos_2)

#####################
query_bens_candidatos = import_query( os.path.join(SRC_DIR, 'candidatos_bens.sql') )
query_bens_candidatos = query_bens_candidatos.format( cargo=args.cargo.upper() )

df_candidatos_bens = pd.read_sql_query( query_bens_candidatos,
                                        con )

(df_candidatos_bens.sort_values( by='total_declarado',
                                 ascending=False )
                   .head(args.n)
                    )