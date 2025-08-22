from carro import Carro #importando a classe Carro

class Pessoa:
    def __init__(self,nome,idade,cidade,exemplo_carro2:Carro):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.exemplo_carro2 = exemplo_carro2

    def apresentar(self):
        print(f"Olá sou a {self.nome} tenho {self.idade} anos e moro {self.cidade}")
    def digirir(self):
        print(f"{self.nome} está diringindo o {self.exemplo_carro2.marca} {self.exemplo_carro2.modelo} {self.exemplo_carro2.cor} {self.exemplo_carro2.ano}")
        self.exemplo_carro2.acelerar
       
meu_carro = Carro ("ford", "fiesta", "vermelho", "2016")
pessoa1 = Pessoa ("Evellyn ", "16", "São Paulo", meu_carro)

pessoa1.apresentar()
pessoa1.digirir()
