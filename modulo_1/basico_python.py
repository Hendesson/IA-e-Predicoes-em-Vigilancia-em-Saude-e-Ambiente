#Variaveis 
idade = 24
nome = "Hendesson"
'''''
#tipos de variaveis 
int = numeros inteiros 
float = numeros com decimais 
str = strings 
bool = true ou false 
'''
#exemplo 
print(type(idade))
print(type(nome))

#Operacoes entre variaveis 
#Soma 
print(2+2)

#Texto e operacao 
print("Subtracao: ", (3 - 2))
print("Mutiplicacao: ", (3*3))
print("Divisao comum: ", (4/2))
print("Divisao inteira:", (4//2))

#calculo IMC 
peso = 61
altura = 1.83

IMC = peso / (altura**2)
IMC = round(IMC,1)

print(IMC)

#Operadores 
a = 1
b = 2

print( a == 1, a!=b) #igual e diferente 
print(a>b, b<a) #maior e igual 

#listas = armazenar valores dentro de uma variavel 
#Ex.: Surto de doença transmitida por alimentos (DTA)

#lista de convidados
covidados = ["alice", "bruna", "matheus", "pedro", "hendesson"]
#lista de quem comeu a maionese
cm_maionese = ["alice","bruna"]
#quem teve sintomas
sintomas = ["alice"]

#Estruturas 

#Estruturas sequencial 
#As linhas sao executadas por ordem 

#Estrutura condicional 
#DECISAO POR CONDICAO 

eu = "hendesson"
if eu in sintomas:
    print("Nao pode entrar")
else:
    print("Pode entrar")

#Estrutura de repeticao
#Loop = repetir uma acao varias vezes
#for = para cada item em uma sequencia 
#while = enquento uma condicao for verdadeira 


for pessoas in covidados:
    if pessoas in cm_maionese and pessoas in sintomas:
        print(pessoas, "comeu e teve sintomas")
    elif pessoas in cm_maionese and not pessoas in sintomas:
        print(pessoas, "comeu e nao teve sintomas")


