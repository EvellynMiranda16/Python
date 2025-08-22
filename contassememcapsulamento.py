class contasemencapsulamento:
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
conta1 = contasemencapsulamento("Evellyn", 1000.00, "1234")    

# consulta com senha correta
conta1.ver_saldo("1234")  

#alterando dados diretamente (problema)
conta1.saldo = 999_999.99
conta1.senha = "0000"
conta1.titular = "novo titular"

#consulta com a senha alterada indevidamente
conta1.ver_saldo("0000")
