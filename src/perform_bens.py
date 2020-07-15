import pandas as pd
import os
import sqlalchemy
import sys
import argparse

pd.set_option('display.float_format', lambda x: '%.3f' % x)

cargos = ['DEPUTADO ESTADUAL',
          'DEPUTADO FEDERAL',
          'VICE-GOVERNADOR',
          'GOVERNADOR',
          'SENADOR',
          'PRESIDENTE',
          'VICE-PRESIDENTE',
          'DEPUTADO DISTRITAL']

parser = argparse.ArgumentParser()
parser.add_argument("--cargo", '-c', help='Nome do cargo', type=str, default="", choices=cargos)
parser.add_argument("--top", '-t', help='Quantidade de tops', type=int)
parser.add_argument("--db", help='Execuçao completa no banco de dados', action='store_true')
parser.add_argument("--save", "-s", help='Salvar o resultado no banco?', action='store_true')
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

print("\n Abrindo conexão com banco de dados...", end="")
con = sqlalchemy.create_engine( "sqlite:///" + os.path.join( DATA_DIR, 'brasilio.db' )  )
print("ok.")

if args.db:
    print("Importanto query...", end="")
    query_bens_candidatos = import_query( os.path.join(SRC_DIR, 'full_query_bens.sql') )
    query_bens_candidatos = query_bens_candidatos.format( cargo=args.cargo.upper(),
                                                          top=args.top )
    print("ok.")
    print("Executando query...", end="")
    result = pd.read_sql_query(query_bens_candidatos, con)
    print("ok.")

else:
    print("Importanto query...", end="")
    query_bens_candidatos = import_query( os.path.join(SRC_DIR, 'candidatos_bens.sql') )
    query_bens_candidatos = query_bens_candidatos.format( cargo=args.cargo.upper() )

    print("ok.")
    print("Executando query...", end="")
    df_candidatos_bens = pd.read_sql_query( query_bens_candidatos,
                                            con )
    print("ok.")

    print("Tratando o dados no pandas...", end="")
    result = (df_candidatos_bens.sort_values( by='total_declarado', ascending=False )
                                .head(args.top)
                        )[['nome', 'total_declarado']]
    print("ok.")

if args.save:
    print("Salvando no banco...", end="")
    result.to_sql('tb_resultado_bens', con, index=True, if_exists="replace")
    print("ok.")

print(result)