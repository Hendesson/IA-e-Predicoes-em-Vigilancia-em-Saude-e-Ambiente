


#No terminal sudo apt install python3-pandas e etc
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder 

#importando um dado e associando a uma variavel 
df = pd.read_csv("/home/alves/Downloads/python/modulo_1/dados_tuberculose.csv", encoding='latin-1', sep=',')

#10 primeiras
print(df.head(10))
#10 ultimas
print(df.tail(10))
#mostrar colunas
print(df.columns)

#mostrar de uma linha pra frente
print(df[10:15])

#acessar coluna

print(df["CS_SEXO"])

#acessar colunas 
print(df[["CS_SEXO", "CS_RACA"]])

#verificar o tipo de dado de uma coluna 
print(df.dtypes)

#converter coluna 


print(df.dtypes)
print(df["DT_DIAG"].head(10))

df["DT_DIAF"] = pd.to_datetime(df["DT_DIAG"])



