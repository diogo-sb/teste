numero = int(input("Digite o numero da taboada que voce quer: "))

contador = 0

while contador <= 9:
    contador = contador + 1
    print(numero, "x", contador, "=", numero * contador)
