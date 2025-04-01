#outras estruturas de dados: Tuplas,conjuntos e dicionários

r = range(1, 9)
print(r)

for intem in r: 
    print(intem)

    lista = lista(r)
    print(lista)

    lista_vazia = []
    lista_vazia = list()
    
    tupla = ()
    tupla = tuple()

    tupla = tuple(r)
    print(tupla)

    lista = ["Ana", "paula", "Sofia"]
    tupla = ("Ana", "paula", "Sofia")

    print(lista)
print(tupla)

lista.append("Isabelly")
tupla #não tem como adicionar, retirar ou modificar apos criação

conjunto = {}
conjunto = set()

conjunto = set(r)
print(conjunto)

conjunto.add(19)
print(conjunto)

dicionario = {}
dicionario = dict()

dicionario = {"SP": "São Paulo", "RJ": "Rio", "ES":"Espirito Santo", "MG": "Minas Gerais"}
print(dicionario)
print(dicionario["SP"])

dicionario_nomes = {0: "Ana", 1: "Maria", 2: "Carol", 3: "Cristal", 4: "Isabelly"}

print(dicionario_nomes[1])

dicionario_paises = {55:"BR", 1: "USA", 23: "UK"}
print(dicionario_paises[55])
#print(dionario_paises[10])