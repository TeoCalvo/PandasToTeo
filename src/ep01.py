import pandas as pd

# Series
int(4.3) 
serie_receita = pd.Series( [1,4,10,2,100000, 200, None], name="receita" )

# Mostrando a série criada
print("Nossa série:\n\n", serie_receita )
print("Tipo da nossa série: ", type(serie_receita))

# DataFrame
dados = {"nome": ['Teo', "Nah", "Code", "Karla"],
         "sobrenome": ["Calvo", "Ataide", "Show", "Mag"],
         "idade": [28, 30, 32, 30]  }

df_pessoas = pd.DataFrame( dados ) # tb_pessoa


## Começando a aula...

# Lendo um csv...
pathfile_csv = "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/meu_treino/PandasToTeo/data/tb_candidatura_2018.csv"
df_candidatura = pd.read_csv( pathfile_csv, sep=";")
df_candidatura.head()

# Lendo um xlsx
pathfile_xlsx = "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/meu_treino/PandasToTeo/data/tb_declaracao_2018.xlsx"
df_declaracao = pd.read_excel(pathfile_xlsx)
df_declaracao.head()

#############################
# Brincando com o DataFrame...
#############################

# Número de linhas para serem exibidas a partir da primeira
df_candidatura.head(2) # Isso é um método

# Numero de linhas para serem exibidas a partir da última
df_candidatura.tail(2) # Isso tbm é um metodo

# Numero de linhas e colunas de um dataframe (tupla)
df_candidatura.shape[0] # Isso é um atributo

# Quais são as colunas do dataframe?? Sabemos que temos 45 colunas
df_candidatura.columns # Outro atributo

# Navegando pelas colunas do DataFrame...
df_candidatura['nome'] # Retorna séries com do nome, ou coluna, melhor dizendo

colunas_selecionadas = ['nome', 'cpf', 'descricao_ocupacao']
df_candidatura[ colunas_selecionadas ].head()

df_candidatura_new = df_candidatura[ colunas_selecionadas ]

# Navegando pelas colunas e linhas do DataFrame...
df_candidatura["nome"][29140] # df[column][index]

# Informações do DataFrame...
df_candidatura.info()