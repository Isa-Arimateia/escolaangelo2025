# Solicita ao usuário o valor do comprimento
# Solicita ao usuário o valor da largura
# Calcula a área do retângulo
# Calcula o perímetro do retângulo
# Exibe o resultado com duas casas decimais

comprimento = int(input("digite o comprimrnto do retângulo: "))
largura = int(input("digite a largura do retângulo: "))

Area = comprimento*largura
Perimetro = 2 * (comprimento + largura)
print(f"A área do retângulo é:{Area: .2f} ")
print(f"o perimetro do retângulo é: {Perimetro: .2f}")

