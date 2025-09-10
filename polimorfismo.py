'''
O que é Polimorfismo?

É quando um mesmo método tem comportamentos diferentes dependendo da classe que o usa.

Pensa assim:

Todas as classes falam de um jeito próprio quando você chama esse método.
'''

class Pessoa:
    def __init__(self, nome): 
        self.nome = nome       

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}.")

class Cliente(Pessoa):
    def apresentar(self):  # mesmo nome, comportamento diferente
        print(f"Sou cliente {self.nome}, estou estudando.")   

class Aluno(Pessoa):
    def apresentar(self):  # mesmo nome, comportamento diferente
        print(f"Sou aluno {self.nome}, estou estudando.") 

# Criando objetos 
P = Pessoa("Robson")
C = Cliente("Jubisvalda")
A = Aluno("Claudio")

# Chamando o MESMO método "apresentar"
P.apresentar()
C.apresentar()
A.apresentar()
