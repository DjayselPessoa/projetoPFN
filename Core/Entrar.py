from time import sleep


class Entrar:

    def entrar(self, nome, senha):
        try:
            self.nome = nome
            self.senha = senha
            status = 0
            cont = 0
            cont1 = 0
            first = True
            entradaNome = str(input("Informe um nome: -> ")).lower()
            for i in self.nome:
                cont += 1
                if first:
                    for i2 in entradaNome:
                        cont1 += 1
                        if i2 == " ":
                            raise ValueError("Não utilize espaço em branco! - REINICIANDO!")
                        if cont1 == len(entradaNome):
                            print("CHECKED!")
                            sleep(1)
                            first = False
                            break

                if i == entradaNome:
                    print("Usuário encontrado!")
                    sleep(1)
                    entradaSenha = str(input("Informe sua senha: -> "))
                    if self.senha[cont - 1] == entradaSenha:
                        status = 1
                        position = cont - 1
                        return status, position
                    else:
                        sleep(1)
                        raise ValueError("SENHA INCORRETA - REINICIANDO!")

            else:
                if cont == len(nome) and status == 0:
                    sleep(1)
                    raise ValueError("DADO INCORRETO! - REINICIANDO!")

        except ValueError as e:
            print("LOG: -> ", e)
        finally:
            return status, position


ObjEntrar = Entrar()
