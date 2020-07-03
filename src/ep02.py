import pandas as pd
import os

endereco_programa = os.path.join( os.path.abspath('.'), 'src')
endereco_programa = os.path.dirname( os.path.abspath(__file__) )

endereco_projeto = os.path.dirname( endereco_programa )
endereco_dados = os.path.join( endereco_projeto, 'data' )

filepath_csv = os.path.join( endereco_dados, 'tb_candidatura_2018.csv')
df_candidatura = pd.read_csv( filepath_csv, sep=";" )