# Crie duas variáveis e atribua valores inteiros divida o maior pela menor e verefique se o resto 
# da divisão deu zero. se deu zero imprima "o numero maior é par", se não imprima "o número maior é impar"

N= 6 
n1= 8

if N > n1:
    modulo = N % n1
else: 
    modulo = n1 % N

if modulo > 0: 
    print ("o número maior é par ")
else: 
    print ("o número menor é impar")


