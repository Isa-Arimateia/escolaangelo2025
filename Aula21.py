# 1.Adicione o nuemro 50 ao final dessa lista 

lista_numeros = [10, 20, 30, 40]
lista_numeros.append(50)
print(lista_numeros)

# 2.Adicione "Laranja" ao indice 1 da lista 

lista_frutas = ["Maça", "banana", "uva"]
lista_frutas.insert(1, "laranja")
print(lista_frutas)

# 3.Remova "cachorro" da lista

lista_animais = ["cachorro", "gato", "Passaro", "cachorro"]
while "cachorro" in lista_animais:
    lista_animais.remove("cachorro")
    print(lista_animais)

# 4.Remova o elemento de indice 2 da lista e mostre o elemento removido.

lista_nomes = ["Alice", "bob", "Charlie", "David"]
nome_removido = lista_nomes.pop(2)
print(f"nome removido da posição 2:{nome_removido}")
print("lista final:", lista_nomes)

# 5.Encontre o indice da primeira ocorrecia de "azul" na lista 

lista_cores = ["vermelho", "azul", "verde", "amarelo", "azul"]
print(lista_cores.index("azul"))

# 6.Conte quantas vezes o numero 2 aparece na lista 

lista_numeros_repetidos = [1, 2, 3, 2, 4, 2, 5, 2]
quantidade = lista_numeros_repetidos.count(2)
print(f"O número 2 aparece {quantidade} vezes na lista.")

# 7.Ordene a lista em ordem crescente. 

lista_desordenarda = [50, 20, 80, 10, 40]
lista_desordenarda.sort()
print(lista_desordenarda)

# 8. Inverta a ordem dos elementos da lista.

lista_invertida = ["maça", "banana", "laranja", "uva"]
lista_invertida.reverse()
print(lista_invertida)
