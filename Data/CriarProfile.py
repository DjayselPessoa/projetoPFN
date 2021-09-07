from Core.EscreverCSV import ObjEscreverCSV
from Core.AbrirCSV import ObjAbrirCSV


class CriarProfile:
    def criarprofile(self, alert):
        try:
            self.alert = alert
            alert = self.alert
            fim = 0
            space = 0
            novoScore = 0
            novoCod = "#" + str(int(alert) + 1)
            nomeTratado = str
            novoNome = str(input("Informe o primeiro nome -> "))
            novoNome = novoNome.lower()
            print(novoNome)
            for i in novoNome:
                print("Ok")
                if str(i) == " ":
                    space += 1
                    nomeTratado = nomeTratado + ""
                if space > 1 and len(nomeTratado) > 0:
                    raise ValueError("Informe somente o primeiro nome - >")
            else:
                print("Nome recebido!")
                nomeTratado = novoNome
            novaSenha =  str(input("Informe a senha -  6 digitos somente números -> "))
            if 6 <= len(novaSenha) <= 6:
                for i in novaSenha:
                    if i in "0123456789":
                        continue
                    else:
                        raise ValueError("ERRO DE COMPOSIÇÂO DE SENHA!")
            else:
                raise ValueError("ERRO DE COMPOSIÇÂO DE SENHA!")

            data = [(novoCod), (nomeTratado), (novaSenha), (novoScore)]
            fim = ObjEscreverCSV.escrevercsv(data)
            if fim == 1:
                raise ValueError("RETORNANDO!")
            else:
                raise ValueError("ERRO! - REINICIANDO!")

        except ValueError as e:
            print("LOG -> ", e)

        finally:
            return alert


ObjCriarProfile = CriarProfile()
