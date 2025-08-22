#o if é usado para executar um bloco de código apenas se uma determinada condição for verdadeira.
#o elif serve para verificar condições adicionais após a primeira condição if ter sido avaliada como falsa.
#o else  é usado em conjunto com a estrutura condicional if para definir um bloco de código a ser executado quando a condição especificada no if for falsa.
#o calculo de multiplicação serve para realizar a operação matemática de multiplicação entre dois ou mais valores, sejam eles números inteiros, decimais ou variáveis.
peso = float(input("Digite o peso em kg:"))
altura = float(input("Digite a altura em metros:"))


imc = altura * altura / peso
imc = round(imc, 2) 

if imc < 18.5: 
    print = "Abaixo do peso"
elif imc  <=18.5 or imc  <25:
    print = "Peso normal"
elif imc <=25 or imc <30:
    print = "Sobrepeso"
else:
    print("Obesidade")
