# EXERCÍCIOS FOR

#  1.Faça um programa que imprima cada elemento da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
#  usando o for.

lista = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
for elemento in lista:
    print(elemento)

#  2. Faça um programa que imprima cada elemento da lista [3, 8, 30, 8, 19, -12, -2, -1, -7, -48] 
# usando o for com range.

lista = [3, 8, 30, 8, 19, -12, -2, -1, -7, -48]
for i in range(len(lista)):
    print(lista[i])

#  3. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista
#  usando o for

lista = [5, 12, -7, 20, 33, -15, 8, 0, 27, -4]
for elemento in lista:
    print(elemento)

#  4. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista
#  usando o for com range

lista = [5, 12, -7, 20, 33, -15, 8, 0, 27, -4]
for i in range(len(lista)):
    print(lista[i])

# 5. Faça um programa que imprima todos os itens da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
#  usando while e compare-o com o exercício 1.

lista = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

#  6. Faça um programa que imprima todos os números de 5 a 0 usando o for.

for i in range(5, -1, -1):
    print(i)

#  7. Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números
#  de 0 a n-1

n = int(input("digite um numero: "))
lista = list(range(n))
print(lista)
# 8. Faça um programa que imprima o maior número da lista [-8, -6, 3, -1, 7], sem usar o método max(). 

lista = [-8, -6, 3, -1, 7]
maior = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero 
# 9. Agora, usando o método max(), faça um programa que imprima os três maiores números
#  da lista [2, 9, -5, 2, -8, 4, -9, -5, 4, 1].

lista = [2, 9, -5, 2, -8, 4, -9, -5, 4, 11]

# Criar uma cópia da lista para não modificar a original
copia_lista = lista.copy()
maiores_numeros = []

# Encontrar os três maiores números
for _ in range(3):
    maior = max(copia_lista)
      # Encontra o maior número
    maiores_numeros.append(maior)  
    copia_lista.remove(maior)  
    9
    # Remove o maior encontrado para procurar o próximo maior

print("Os três maiores números são:", maiores_numeros)