# Exercícios

#  1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. 
# Concatene-as e imprima o resultado.
str1 = "Olá"
str2 = "Mundo"
resultado = str1 + " " + str2
print(resultado)  

#  2. Dada a string “Python”, imprima o caractere que está no índice 2.
palavra = "Python"
print(palavra[2]) 

#  3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.
string = "exemplo"
string = string.replace("e", "a")
print(string)

#  4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.
nome = input("Digite seu nome: ")
print(len(nome)) 

#  5. Crie uma string que represente uma frase.
#  Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)
frase = "O cachorro correu pelo quintal."
print("gato" in frase)  

#  6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.
frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavra))
print(palavra)

#  7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas.
#  Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.
def inverter_palavras(frase):
    return " ".join(frase.split()[::-1])
print(inverter_palavras("Olá Mundo"))  

#  8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final.
#  Remova esses espaços e imprima a string resultante.
string = input("digite uma string com espaços no início e no final: ")
print(string)
print(string.strip() + "!")

#  9. Crie uma função que receba um número inteiro e retorne uma string que o 
# represente com separadores de milhares. Por exemplo, para o número 1234567, 
# a função deve retornar “1,234,567”.
numero= 1234567
print(f"{numero:,}")
            