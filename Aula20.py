#Exercícios 

# 1. Na lista pares = [0,2,4,8]:
# a) Acrescentando o valor 10 ao final d lista 
# b) Acrescentar o valor 6 na posição

pares = [0,2,4,8]
pares.append(10)
pares.insert(3, 6)
print(pares)


# 2. Na lista ímpares = [1, 3, 3, 5, 7, 9]
# a) Remova o valor três 
# b) Remova o valor da posição (índice 4)
# c) mostre o valor que será removido da posição (índice)

ímpares = [1 , 3 ,3, 5, 7, 9]
ímpares.remove(3)
valor_removido= ímpares.remove(ímpares[4])
print(f"valor removido da posição 4:{valor_removido}")
print("lista final:", ímpares)

# 3. Na lista fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]:
# a) Ordene a lista 
# b) coloque em valor reverso a lista fibonacci

fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
fibonacci.sort()
print(fibonacci)
fibonacci.reverse() 
print(fibonacci)

# 4. Na lista pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]:
# a) Busque o elemento que esta no índice 5 da lista 
# b) Imprima o tamanho da lista 
# c) Imprima o valor máximo da lista 
# d) Imprima o valor mínimo da lista 
# e) Imprima apenas o resultado [4,5]

pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(pi[5])
tamanho_lista = (len(pi))
print(tamanho_lista)
valor_máximo =  (max(pi))
print(valor_máximo)
valor_mínimo = (min(pi))
resultado = pi[2:4]
print("Resultado [4, 5]:", resultado)
