class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas


# Teste do código
perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')
perfil.curtir()
perfil.curtir()
print(perfil.obter_curtidas())  # Saída: 2


#burlando a curtida 

perfil._Perfil__curtidas += 10  
print(perfil.obter_curtidas())
