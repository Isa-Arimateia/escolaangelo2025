# Exercícios

#  1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. 
# Concatene-as e imprima o resultado.
str1 = "Olá"
str2 = "Mundo"
resultado = str1 + " " + str2
print(resultado)  # Saída: Olá Mundo

#  2. Dada a string “Python”, imprima o caractere que está no índice 2.
palavra = "Python"
print(palavra[2])  # Saída: t

#  3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.
texto = "casa"
novo_texto = texto.replace("a", "o", 1)  # Substitui apenas a primeira ocorrência de 'a' por 'o'
print(novo_texto)  # Saída: cosa

#  4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.
nome = input("Digite seu nome: ")
print(len(nome))  # Exibe o número de caracteres no nome

#  5. Crie uma string que represente uma frase.
#  Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)
frase = "O cachorro correu pelo quintal."
print("gato" in frase)  # Saída: False

#  6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.
frase = input("Digite uma frase: ")
num_palavras = len(frase.split())
print(f"Número de palavras: {num_palavras}")

#  7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas.
#  Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.
def inverter_palavras(frase):
    return " ".join(frase.split()[::-1])
print(inverter_palavras("Olá Mundo"))  # Saída: Mundo Olá

#  8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final.
#  Remova esses espaços e imprima a string resultante.
texto = input("Digite uma string com espaços: ")
print(texto.strip())  # Remove os espaços extras no início e no final

#  9. Crie uma função que receba um número inteiro e retorne uma string que o 
# represente com separadores de milhares. Por exemplo, para o número 1234567, 
# a função deve retornar “1,234,567”.
def formatar_numero(numero):
    return f"{numero:,}"
print(formatar_numero(1234567))  # Saída: 1,234,567

#  10. Implemente uma função que receba uma string e um número 
# (chamado de “deslocamento”) como parâmetros e retorne a string cifrada, 
# usando a Cifra de César. Cada letra na string deve ser deslocada pelo número fornecido.
#  Por exemplo, com um deslocamento de 3, “ABC” seria cifrado como “DEF”
def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado
print(cifra_de_cesar("ABC", 3))  # Saída: DEF

# 11. Escreva um programa que receba uma palavra ou frase
#  do usuário e determine se ela é um palíndromo ou não. 
# O programa deve ignorar maiúsculas e minúsculas, bem como espaços em branco
def eh_palindromo(texto):
    texto_limpo = "".join(texto.lower().split())
    return texto_limpo == texto_limpo[::-1]

print(eh_palindromo("Ame a ema"))  # Saída: True