#variavel: um nome que se refere a um valor armazenado na memória.
#para atribuir um valor na variavel e´necessario usar o sinal de =.
#o float é usado para pegar o valor em texto e transformar em numeros decimais.
#o print é usado para exibir informações na tela, seja no terminal, console ou qualquer outra saída padrão.
#o format é utilizado para formatar strings, inserindo valores de variáveis ou expressões em posições específicas dentro da string.
#o input serve para obter dados inseridos pelo usuário através do teclado, permitindo que o programa interaja de forma dinâmica com o usuário. 
fahrenheit=float(input("digite a temperatura: "))

celsius =(fahrenheit-32)*5/9

print("a conversão é: ", format(celsius, ".2f"))