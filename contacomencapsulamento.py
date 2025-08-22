class contacomencapsulamento:
    def _init_(self,titular,saldo,senha):
        #todos são publicos
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def ver_saldo(self,senha_digitada):
        #verifica se a semha esta correta
        if senha_digitada == self.senha: 
            print(f"saldo de (self.titular): R$(self.saldo:.2f)")
        else:
            print("senha incorreta! Acesso negado.")    

#teste
conta2 = contacomencapsulamento("Evellyn", 1000.00, "1234")    

# consulta com senha correta
conta2.ver_saldo("1234")  

#alterando dados diretamente (problema)
conta2.saldo = 999_999.99
conta2.senha = "0000"
conta2.titular = "novo titular"

#consulta com a senha alterada indevidamente
conta2.ver_saldo("0000")

class contabancaria:
    def _init_(self,titular,saldo_inicial, senha):
        #publico: pode ser acessado livremente
        self.titular = "titular"

# protegido: não deve ser alterado diretamente
        self._saldo = float ("saldo_inicia")      

# privado: não pode ser acessado diretamente
        self._senha = str("senha")

    def ver_saldo(self,senha_digitada):
        #verifica se a senha esta correta
        if senha_digitada == self.senha: 
            print(f"saldo de (self.titular): R$(self.saldo:.2f)")
        else:
            print("senha incorreta! Acesso negado.")    

#alterando o publico (permitido)
conta2._saldo = 50,00
conta2.ver_saldo("1234")
