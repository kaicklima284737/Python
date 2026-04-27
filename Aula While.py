"""
#Implemente algoritmos em Python utilizando a estrutura de repetição While

#1. Escreva um algoritmo que exibe os números inteiros de 1 a 20.

Cont = 1

while Cont <=20:
 print(Cont)
 Cont += 1

#2. Escreva um algoritmo que solicite 10 números e exiba o dobro de cada número digitado.
N = 0
Cont = 1

while Cont <= 10:
 Num = float(input(f"Digite o {Cont}° número: "))
 duplo = Num * 2
 print(duplo)
 Cont +=1

print("Fim")

#3. Escreva um algoritmo que solicite a idade de 15 pessoas e informe a quantidade de pessoas com idade inferior a 18 anos.
Cont = 1
Idade_18 = 0

while Cont <= 15:
 I = int(input(f"Informe a {Cont}° Idade: "))
 if I < 18:
  Idade_18 +=1
 Cont += 1

print(f"temos Ao todo {Idade_18} menores de idade")

# 4. Escreva um algoritmo que solicite 10 números e informe quantos números entre 100 e 200 foram digitados.
Cont = 1
Numeros = 0

while Cont <=10:
 N = int(input(f"Informe o {Cont}° Número: "))
 if N >=100 and N <=200:
  Numeros +=1
 Cont +=1

print(f"Teve {Numeros} Números entre 100 e 200.")

#5. Escreva um algoritmo que solicite 15 números e informe o somatório de todos os números ímpares digitados.

Cont = 1
Soma = 0

while Cont <= 15:
 numero = int(input(f"Informe o {Cont}° número: "))
 if numero % 2 != 0:
   Soma += numero
 Cont += 1

print(f"A soma dos números Impares é igual a {Soma}")

#6. Solicite vários números ao usuário (até que ele digite o número zero) e informe o somatório dos números digitados.

numero = 1
soma = 0
while numero != 0:
 numero = int(input("Informe um número: "))
 soma += numero

print(f"Somátoria de todos os números diferentes de 0 : {soma}")



#7. Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo
# deve solicitar os números novamente) e informe a diferença entre o maior e o menor número.

numero_1 = 0
numero_2 = 0

while numero_2 == numero_1:
    numero_1 = int(input("Informe um número: "))
    numero_2 = int(input("Informe um número: "))
    if numero_1 == numero_2:
        print(" Números Iguais, digite novamente")

if numero_1 > numero_2:
    N = numero_1 - numero_2
else:
    N = numero_2 - numero_1

print(f"A difença do maior pro menor:{N}")


#8. Escreva um algoritmo que solicite 10 números e informe qual foi o menor número digitado.

cont = 1
Numero = 100
while cont <=10:
    N = int(input("Digite um Número: "))
    if N < Numero:
        Numero = N
    cont += 1

print(f"O menor número foi: {Numero}")

#9. Faça um algoritmo que solicite N números e calcule a média dos números pares e a
#média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do programa).





10. Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 5
centímetros por ano. Considerando que Chico e Juca continuem crescendo
constantemente, escreva um algoritmo que calcule quantos anos seriam necessários
para Juca ser mais alto que Chico.
11. Escreva um programa que solicita ao usuário o valor de N e calcule o valor de 𝑆 na série
abaixo:

12. Faça um algoritmo que solicite um número inteiro ao usuário e calcule o fatorial desse
número. O fatorial de um número N é a multiplicação de N por seus antecessores
maiores ou iguais a 1.
Por exemplo: o fatorial de 5 é igual a 5*4*3*2*1 = 120
"""




"""
1. Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é fornecido pelo usuário.
2. Fazer um algoritmo que solicite um número inteiro N qualquer e exiba a tabuada de N.
Exemplo: para N = 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
"""
#3. Construa um algoritmo que mostre todos os valores ímpares entre X e Y, onde X e Y são fornecidos pelo usuário.
"""
X = int(input("Informe um Número:"))
Y = int(input("Informe outro Número:"))
cont = 

if Y > X:
    Z = Y
    Y = X
    Z = X

if X%2 == 0:
    X+1

while cont > Y and cont < X:
    print(X)
    X -= 2

A = int(input("Informe um Número:"))
B = int(input("Informe outro Número:"))

if A > B:
    C = A
    A = B
    B = C

if A == B:
    print("Os Números São Iguais.\nNão existem Impares entre eles")
else:
    if A % 2 == 0:
        A += 1

    while A <= B:
        print(A)
        A += 2





"""

#4. Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva se o número lido é um número
#perfeito ou não. Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao próprio
#número. Exemplo: 6 é um número perfeito porque 1 + 2 + 3 = 6.

Int = int(input("Informe um Número positivo: "))
Soma = 0
while Int <= 0:
    Int = int(input("Número Inválido!! Informe um Número positivo: "))
Cont = 1

while Cont < Int:
    if Int%Cont == 0:
        Soma += Cont
    Cont += 1

if Soma == Int:
    print(f"O número {Int} é um Número perfeito.")
else:
    print(f"O número {Int} não é um Número perfeito.")



# Somar todos os divisores de Int, ou seja, se não houver resto é um divisor de Int


"""
5. Fazer um algoritmo que solicite um número indeterminado de idades de um grupo de indivíduos. A última idade, 
que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule a média de idade deste grupo de 
indivíduos.
6. Número primo é aquele que somente é divisível por 1 e por ele mesmo. Fazer um algoritmo que solicite um 
número e informe se esse número é primo ou não.

#7. Solicite um número inteiro positivo e informe a soma dos algarismos desse número. Por exemplo:
#Entrada: 1234 Saída: 10
#Entrada: 2182341 Saída: 21
#Entrada: 100001 Saída: 2

N = int(input("Informe un múmero Inteiro Positivo: "))
soma = 0

while N <= 0:
    N = int(input("Número Invalido!! Escreva um número Positivo maior que 0: "))

while N > 0:
    S = N % 10
    soma += S
    N = N // 10

print(f"A Soma dos Algarismos é: {soma}")




8. Escreva um algoritmo que solicite vários números inteiros e exiba o resultado da multiplicação de todos os 
números ímpares e o somatório de todos os números pares. O algoritmo deve ser finalizado quando o usuário 
digitar zero.
9. Faça um algoritmo que apresente um menu com as opções abaixo. Considere que o saldo deve iniciar em R$ 
0,00 e a cada saque ou depósito o valor do saldo deve ser atualizado. Após cada operação realizada, o menu 
deve ser exibido novamente, e o programa deve ser finalizado apenas quando o usuário selecionar a opção 4.
1 - Consulta Saldo 
2 - Realizar Saque 
3 - Realizar Depósito 
4 – Sair
Escolha uma opção: 
10. Faça um algoritmo para uma eleição entre três candidatos. Deve ser exibido um menu com as opções abaixo. 
1 - Candidato 1
2 - Candidato 2
3 - Candidato 3
4 - Voto em Branco
5 - Finalizar
Informe o seu voto: 
Quando for escolhida a opção 5, a eleição deve ser finalizada e as informações abaixo devem ser exibidas:
a) A quantidade de votos de cada candidato
b) A porcentagem de votos brancos
c) O candidato vencedo
"""