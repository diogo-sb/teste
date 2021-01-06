"R$ {:f}".format() #pra reconhecer o numero e ser float mas com isso vai ter 00000 a direita
"R$ {:.2f}".format() #pra formatar e mostrar só os 2 numeros depois da virgula
"R$ {:7.2f}".format() #contando a quantidade dos numeros e depois definindo 2 numeros depois da virgula
"R$ {:07.2f}".format() # colocando 0 a esquerda mesmo se ele nao tivesse o tamanho de 7 caracteres
"R$ {:07d}".format() #a letra d significa q é um numero inteiro e não float
"Data {:02d} / {:02d}".format() #estou definindo o formato de 2 digitos e mostrando o 0

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo")) #invertendo os valores na saida q começa no 0 e com isso o nome esta vindo primeiro






