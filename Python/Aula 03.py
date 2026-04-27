#Exercício 01


"""
CP1 = float(input("Informe a nota do cp1: "))
CP2 = float(input("Informe a nota do cp2: "))
Sprint1 = float(input("informe a nota do Sprint1: "))
Sprint2 = float(input("informe a nota do Sprint2: "))
GS1 =  float(input("informe a nota do GS1: "))

M1 = ((CP1+CP2)/2)*0.2 + ((Sprint1+Sprint2)/2)*0.2 + GS1*0.6

print ("Sua média é:", M1)


#Exercicío 02


Valor = float(input("Infore o valor do Produto:R$ "))

Valor_Desconto = Valor - Valor*0.12

#print("O preço do produto com desconto é R$ ",Valor_Desconto)
print(f"O preço do produto com desconto é R$ {Valor_Desconto:.2f}")


#Exercicío 03


Int_Segundos = float(input("Insira um valor inteiro em segundos: "))

Horas = Int_Segundos // 3600

Minutos = (Int_Segundos // 60) % 60

segundos = Int_Segundos % 60

print(f"O valor de {Int_Segundos} é igual a {Horas} Horas,{Minutos} Minutos e {segundos} Segundos f")




#Exercício 4


# Chip pé direito Identificação, Identificação R$0.40
# 2 Chips pé esquerdo Alimento R$0.35

Franja = float(input("Quantos Frangos Foram Marcados: "))

PE = (Franja * 2) * 0.35
PD = Franja * 0.40

Gasto = PE + PD

print(f"O valor gasto total na Granja foi de R${Gasto:.2f}")


#Exercício 5


#Escrever um valor em Real e transformar na Cotação de Dolar

Real = float(input("Qual o Valor de Reais? R$ "))

Dolar = float(Real / 5.22)

print(f"O valor de R${Real}Reais na cotação do Dólar em 03/26 é igual a US {Dolar:.2f} Doláres")



#Exércicio 6

#Escrever um Algoritmo que leia os Números de Votos Branco, nulos e validos
# em uma Eleição com o percentual em relação ao total dos votos.

Branco = float(input("Qual o valor de votos Brancos? "))
Nulo = float(input("Qual o valor de votos Nulos? "))
Valido = float(input("Qual o valor de votos Válidos? "))

Votos = float(Branco + Nulo + Valido)

branco_porcentagem = (Branco / Votos) * 100
Nulo_porcentagem = (Nulo / Votos) * 100
Valido_porcentagem = (Valido / Votos) * 100

print(f"O valor de votos totais é igual á {Votos}")
print(f"A porcentagem de Votos Brancos em relação ao total é igual a {branco_porcentagem:.2f} %")
print(f"A porcentagem de Votos Nulos em relação ao total é igual a {Nulo_porcentagem:.2f} %")
print(f"A porcentagem de Votos Válidos em relação ao total é igual a {Valido_porcentagem:.2f} %")



#Exércicio 7


#Ler o valor do raio de um circulo e calcular o valor da área
# Formula = π * raio², com π = 3.1415

raio = float(input("Qual o valor do Raio do Círculo: "))

_pi= 3.1415

Resultado = (raio ** 2) * _pi

print(f"O valor da Área do Circulo com raio igual á {raio} é igual a {Resultado:.2f}")
"""


#Exércicio 8

#Ler o aumento do salário de um Fúncionario sabendo que ele teve um aumento de 25%.

