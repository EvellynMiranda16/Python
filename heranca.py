# Classe Pai (superclasse)
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def apresentar (self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
# Classe Cliente ((herda pessoa)
class Cliente (Pessoa):
    def __init__(self, nome, idade, saldo):
        # Chamando o construtor da classe pai
        super().__init__ (nome,idade)       
        self.saldo = saldo
    def mostrar_saldos(self):
        print(f"{self.nome} tem um saldo de R$ {self.saldo:.2f}")

# Classe Aluno (Herda de pessoa)     
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        # Chamando o construtor da classe pai
        super().__init__(nome, idade)
        self.matricula = matricula  

    def estudar(self):
        print(f"O aluno {self.nome}, matrícula {self.matricula}, está estudando!")     

# Criando objetos
p1 = Pessoa("Carlos", 40)        
c1 = Cliente("Maria", 30, 1500.50)
a1 = Aluno("João", 20, "A12345")

# Executando métodos
p1.apresentar()
print()

c1.apresentar()    # herdada da classe pessoa
c1.mostrar_saldos()
print()

a1.apresentar()    # herdada da classe pessoa
a1.estudar()
