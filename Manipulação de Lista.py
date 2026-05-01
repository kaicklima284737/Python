lista = [3, 10, 7, 8, 1, 9, 8, 5, 8]

crescente = lista[0]

decrescente = lista[0]

menor = lista[0]

maior = lista[0]

soma = 0

for item in lista:
    #encontrar menor item da lista
    if menor > item:
        menor = item
    #encontrar maior item da lista
    if maior < item:
        maior = item
    #somar todos os items da lista
    soma += item
    #Organizar do maior pro menor

for crescente in range(len(lista)):
    for j in range(len(lista)):
        if lista[crescente] < lista[j]:
            x = lista[crescente]
            lista[crescente] = lista[j]
            lista [j] = x






print(f"O menor valor é: {menor} \nO menor valor é: {maior} \nA soma dos números na lista é igual a: {soma}\n"
      f"Ordem crescente: {crescente}")
