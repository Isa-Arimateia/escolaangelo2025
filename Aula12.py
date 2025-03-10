idade = int(input("digite a sua idade:"))

if idade >= 18: 
    print("é de maior")
else:
    print("é de menor.")

numero = int(input("digite um numero:"))

if numero >= 0:
    print ("ele é positivo")
else: 
    print ("ele é negativo") 
        
numero = int(input("digite um número inteir"))
if numero % 2 == 0:
    print("o numero én par")
else:
    print("o numero é impar")



numero1 = int(input("peça um numero:"))
numero = int(input("peça outro numero"))

if numero1 > numero:
    print("é maior")
else:
    print("é menor")

idade= int(input("digita a idade maior que 0 menor que 150"))
if idade > 0 and idade < 150:
    print ("idade válida")
else:
    print("idade inválida")

salário = int(input("digita salário: R$"))
if salário > 0:
    print("é maior que 0")
else:
    print("não é maior que 0")

    salário = int(input("digita salário: R$"))
if salário > 0:
    print(F("O sálario é R$ {sálario}"))
else:
    print("sálario inválido")
sexo = input("digite o sexo [M, F outro;]")
if sexo == "M":
    print("sexo masculino")
elif sexo == "F":
    print("sexo feminino")
elif sexo == "outro":
    print()

