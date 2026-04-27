"""
ALGORITMOS E PROGRAMAÇÃO
Resolva os algoritmos abaixo utilizando a estrutura de repetição for.

1. Escreva um algoritmo que exiba todos os números inteiros de 0 a 50.
for number in range(51):
    print(number)

2 e 3. Escreva um algoritmo que exiba todos os números impares e inteiros de 200 a 100 (em ordem decrescente).

for number in range(200-1,99,-2):
    print(number)


4. Escreva um algoritmo que exiba 20 números aleatórios sorteados entre 1 e 50 (Dica: importe a
biblioteca random).

import random
random (I)
for I in range(1, 51):

5. Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada
de cada número (Dica: importe a biblioteca math).
6. Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.

Number = int(input(f"Informe o 1° Número: "))
maior = Number
menor = Number

for i in range(2,11):
    Number = int(input(f"Informe o {i}° Número: "))
    if Number > maior:
        maior = Number
    elif Number < menor:
        menor = Number

print(f"O maior número digitado foi: {maior}\n"
      f"O menor número digitado foi: {menor}")


7. Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.
8. Escreva um algoritmo que determine se um número N (informado pelo usuário) é primo ou não.
9. Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.


N = -1
Fator = 1

while N < 0:
    N = int(input("Digite um número positivo para calcular o fatorial: "))

if N == 0 or N == 1:
    print("Fatorial de 0 é igual a 1.")
else:
    for N in range(N, 0, -1 ):
        Fator *= N
print(f"O Fatorial de {N} é igual a {Fator}")


10. Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as
suas notas e exiba a sua respectiva média.
"""