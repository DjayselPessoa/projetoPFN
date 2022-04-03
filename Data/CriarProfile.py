from Core.EscreverCSV import ObjEscreverCSV
from time import sleep


class CriarProfile:
    def criarprofile(self, alert, pegarDirRaiz):
        try:
            self.pegarDirRaiz = pegarDirRaiz
            self.alert = alert
            fim = 0

            novoCod = "#" + str(int(self.alert) + 1)
            novoScoreName = "score_"+novoCod+".csv"
            nomeTratado = ""
            sleep(1)
            novoNome = str(input("Informe seu nome -> "))
            print("nome não tratado: ", novoNome)
            novoNome = novoNome.lower()
            novoNome = novoNome.lstrip(' ')
            novoNome = novoNome.rstrip(' ')
            novoNome = str(novoNome.replace(" ", "_"))
            print(f"nome tratado: \n{novoNome}")

            # print(novoNome)
            cont01 = 0
            nomeProcess = ""
            for i in novoNome:
                # print("Ok")
                nomeProcess = nomeProcess + str(i)
                if cont01 == 10:
                    print(f"Processando nome -> {nomeProcess}")
                    sleep(1)
                    print("- 10 caracteres salvos -")
                    novoNome = nomeProcess
                    break
                cont01 += 1
            sleep(0.5)
            print("Nome recebido e devidamente processado!")
            nomeTratado = novoNome
            sleep(1)
            novaSenha = str(input("Informe a senha -  6 digitos somente números -> "))
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
