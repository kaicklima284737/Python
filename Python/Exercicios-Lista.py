"""
EXERCÍCIOS – LISTAS
_______________________________________________________________

Exercício 01

Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e
os números ímpares em outra lista. Exiba as duas listas ao usuário.

___

pares = []
impares = []

for n in range(1,11):
    numero = int( input(f"Informe o {n}° número inteiro: "))

    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)

_______________________________________________________________

Exercício 02

Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a. A média aritmética dos números armazenados na lista.
b. O somatório dos números pares armazenados na lista.

___

"""

"""
_______________________________________________________________

Exercício 03

Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
a. a lista com todos os itens armazenados.
b. o somatório de todos os números contidos na lista.
c. o maior número da lista.
d. o menor número da lista.
"""

"""
_______________________________________________________________

Exercício 04

Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as
idades em outra lista.
Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual
a 18 anos.
"""

"""
_______________________________________________________________

Exercício 05

Preencha a lista com 10 números aleatórios. Na sequência, solicite um número ao
usuário e informe quantas vezes esse número aparece na lista.
"""

"""
_______________________________________________________________

Exercício 06

Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma
nota menor que zero). Após a entrada de dados, exiba:
a. A quantidade de notas que foram informadas.
b. Todas as notas na ordem em que foram informadas.
c. A média aritmética de todas as notas.
d. A quantidade de notas acima da média aritmética calculada.
"""

#--------------------------------------
#Aula 17- Mais Exércicios complementares de Lista.
#--------------------------------------
"""
EXERCÍCIOS COMPLEMENTARES – LISTAS

Exercício 01

Preencha uma lista com 10 números aleatórios únicos (sorteados de 1 a 20), ou seja,
sem elementos repetidos.

_______________________________________________________________

Exercício 02

Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
A partir dessa lista, gere uma nova lista contendo apenas os números primos da lista.
_______________________________________________________________

Exercício 03

Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
A seguir solicite um número inteiro e multiplique todos os itens da lista por esse número.
_______________________________________________________________

Exercício 04

Preencha uma lista com 10 itens e verifique se ela é um palíndromo, ou seja, se ela é
igual quando lida da esquerda para a direita e da direita para a esquerda.

_______________________________________________________________

Exercício 05

Preencha duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.
"""