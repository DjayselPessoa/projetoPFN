class Entrar:

    def entrar(self, nome, senha):
        try:
            self.nome = nome
            nome = self.nome
            self.senha = senha
            senha = self.senha
            status = 0
            cont = 0
            cont1 = 0
            vaga = 0
            first = True
            entradaNome = str(input("Informe seu nome: -> ")).lower()
            for i in nome:
                cont += 1
                if first:
                    for i2 in entradaNome:
                        cont1 += 1
                        if i2 == " ":
                            vaga += 1
                        if vaga > 1:
                            raise ValueError("Não utilize espaço em branco! - REINICIANDO!")
                        if vaga == 0 and cont1 == len(entradaNome):
                            print("Nome correto!")
                            first = False
                        else:
                            continue

                if i == entradaNome:
                    print("Usuário encontrado: -> ")
                    entradaSenha = str(input("Informe sua senha: -> "))
                    if senha[cont - 1] == entradaSenha:
                        status = 1
                        position = cont
                        return status, position
                    else:
                        if status == 0:
                            raise ValueError("SENHA ERRADA! - REINICIANDO!")
                else:
                    if cont == len(nome) and status == 0:
                        raise ValueError("NADA ENCONTRADO - REINICIANDO!")

        except ValueError as e:
            print("LOG: -> ", e)
        finally:
            return status, position


ObjEntrar = Entrar()