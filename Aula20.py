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

