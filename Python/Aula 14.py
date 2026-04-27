"""
1. Faça um programa que some todos os números inteiros positivos abaixo de 1000 que
são múltiplos de 3 ou 5.

for i in range(3,1000):
    if i%3 == 0 or i%5 == 0:
        print(f"Número: {i}")


2. Faça um programa que exiba todos os números primos menores que 1000.
"""
from sqlalchemy.sql.operators import truediv

"""
print("2")
print(2)  # Começamos exibindo o único primo par

for i in range(3, 1001, 2):  # Percorremos apenas os ímpares de 3 a 1000
    e_primo = True

    for n in range(2, i):
        if i % n == 0:
            e_primo = False
            break

    if e_primo:
        print(i)

3. Um funcionário foi contratado em 2015 com um salário de R$ 2000,00. Em 2016 ele
recebeu um aumento de 1.5%. A partir de 2017, os aumentos sempre correspondem ao
dobro da porcentagem do ano anterior. Faça um algoritmo que determine o salário do
funcionário no ano de 2024.

#2000, 1.5% que drobra de porcentagem todo ano
salario_atual = 2000
salario_fixo = 2000
taxa = 0.015

print("-----Juros Compostos-----")
for i in range(2016,2025):
    if i > 2016:
        taxa *= 2

    aumento = salario_atual * taxa
    salario_atual += aumento
    print(f"Ano: {i} | Taxa: {taxa*100:.1f}% | Salario: {salario_atual:.2f}")
print(f"O Valor final no ano de {i} é igual a: R${salario_atual:.2f}")


salario_fixo = 2000
taxa = 0.015
print("-----Juros Simples-----")
for i in range (2016, 2025):

    if i > 2016:
        taxa *= 2

    salario_atual = 2000
    aumento = salario_fixo * taxa
    salario_atual += aumento

    print(f"Ano: {i} | Sálario base:R$2000.00 | Taxa: {taxa*100:.1f} | Sálario atual: {salario_atual:.2f}")
print(f"Resultado final: Ano: {i} | Salário final: R${salario_atual:.2f}")
"""
"""
4. Faça um programa que some todos os números primos existentes entre a e b, onde a e
b são números informados pelo usuário.

a = int(input("Informe um valor: "))
b = int(input("Informe um outro valor: "))
c = 0
soma = 0

while a == b:
    print(f"Informe números diferentes!!!")
    a = int(input("Informe um valor: "))
    b = int(input("Informe um outro valor: "))

if a > b:
    c = a
    a = b
    b = c

for i in range(a, b+1):
    if i < 2:
        continue
    e_primo = True
    for n in range(2, i):
        if i % n == 0:
            e_primo = False
            break
    if e_primo:
        print(f"Primo encontrado: {i}" )
        soma += i
print(f"Valor da Soma dos primos entre {a} a {b}: {soma}")

5. Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar
acertar qual o número foi gerado. A cada tentativa o programa deverá informar se o
número gerado é maior ou menor que o chute do usuário. O programa acaba quando o
usuário acertar o número gerado. Ao final, o programa deve informar em quantas
tentativas o número foi descoberto.
"""
import random

aleatorio = random.randint(1, 100)
numero = 0
b = 0
while b != aleatorio:
    b = int(input("informe um número: "))
    if b > aleatorio:
        print("Errou!!! Informe um Número Menor")
    if b < aleatorio:
        print("Errou!!! Informe um Número Maior")

print("Acertou Mizeravi!!!")
print(f"Numero correto: {aleatorio}")
