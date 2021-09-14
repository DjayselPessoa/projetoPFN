from Core.EscreverCSV import ObjEscreverCSV
from time import sleep


class CriarProfile:
    def criarprofile(self, alert, pegarDirRaiz):
        try:
            self.pegarDirRaiz = pegarDirRaiz
            self.alert = alert
            fim = 0
            space = 0
            novoCod = "#" + str(int(self.alert) + 1)
            novoScoreName = "score_"+novoCod+".csv"
            nomeTratado = str
            sleep(1)
            novoNome = str(input("Informe o primeiro nome -> "))
            novoNome = novoNome.lower()
            # print(novoNome)
            for i in novoNome:
                # print("Ok")
                if str(i) == " ":
                    space += 1
                    # nomeTratado = nomeTratado + ""
                if space > 1:
                    sleep(1)
                    raise ValueError("- Informe o nome sem usar espaço -\nREINICIANDO!")
            else:
                sleep(1)
                print("Nome recebido!")
                nomeTratado = novoNome
            sleep(1)
            novaSenha = str(input("Informe a senha -  6 digitos somente de números -> "))
            if 6 <= len(novaSenha) <= 6:
                for i in novaSenha:
                    if i in "0123456789":
                        continue
                    else:
                        sleep(1)
                        raise ValueError("ERRO DE COMPOSIÇÂO DE SENHA!")
            else:
                sleep(1)
                raise ValueError("ERRO DE COMPOSIÇÂO DE SENHA!")

            data = [(novoCod), (nomeTratado), (novaSenha), (novoScoreName)]
            fim = ObjEscreverCSV.escrevercsv(data, pegarDirRaiz)
            if fim == 1:
                sleep(1)
                raise ValueError("RETORNANDO!")
            else:
                sleep(1)
                raise ValueError("ERRO! - REINICIANDO!")

        except ValueError as e:
            print("LOG -> ", e)

        finally:
            return self.alert


ObjCriarProfile = CriarProfile()
