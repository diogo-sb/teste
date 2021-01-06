import math

a = int(input("Digite o primeiro ponto de A: "))
b = int(input("Digite o segundo ponto de A: "))
y = int(input("Digite o primeiro ponto de y: "))
z = int(input("Digite o segundo ponto de y: "))

resultado = (y - a) ** 2 + (z - b) ** 2

if math.sqrt(resultado) >= 10:
    print("longe")
else:
    print("perto")

