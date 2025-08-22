#o int é um tipo de dado que representa números inteiros, ou seja, números sem casas decimais.
#o for é usado para iterar sobre uma sequência (como listas, tuplas, strings, dicionários, etc.) ou qualquer objeto iterável, executando um bloco de código para cada elemento da sequência. 

numero = int(input("Digite um número inteiro: "))


multiplicadores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


print()
print("Tabuada do número", numero)
print()

for i in multiplicadores:
 resultado = numero * i
print(numero, "x", i, "=", resultado)
