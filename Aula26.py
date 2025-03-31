#  Você está construindo um sistema de gerenciamento de contatos. 
# Crie um programa que realize as seguintes tarefas:

#  a) Peça ao usuário para digitar seu nome completo.
nome_completo = input("digite seu nome completo:")

#  b) Concatene “Olá,” com o nome fornecido e exiba o resultado.
print("Olá", nome_completo)

#  c) Conte quantos caracteres existem no nome completo digitado e exiba o resultado.
num_caracteres = len(nome_completo)
print("O numero de caracteres no se nome é:", num_caracteres)

#  d) Peça ao usuário para digitar um sobrenome para procurar na string do nome completo.
sobrenome = input("Digite seu sobrenome para procurar ser procurado no seu nome completo:")

#  e) Verifique se o sobrenome fornecido está presente no nome completo e exiba uma mensagem apropriada.
if sobrenome in nome_completo:
    print(f"O sobrenome '{sobrenome}'  está presente no nomecompleto")
else: 
    print(f"O sobrenome '{sobrenome}' NÃO está presente no nome completo")

#  f) Exiba o nome completo em letras maiúsculas.
print("seu nome completo em letras maiúsculas:", nome_completo.upper())

#  g) Substitua todas as ocorrências da vogal “a” na string do nome completo pelo caractere ‘4’ 
# e exiba o resultado
nome_completo = nome_completo.replace("a", "4")
print("nome completo com 'a' substituido por '4':",nome_completo)
