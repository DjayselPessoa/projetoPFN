from Core.EscreverCSV import ObjEscreverCSV


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
            novoNome = str(input("Informe o primeiro nome -> "))
            novoNome = novoNome.lower()
            # print(novoNome)
            for i in novoNome:
                # print("Ok")
                if str(i) == " ":
                    space += 1
                    nomeTratado = nomeTratado + ""
                if space > 1 and len(nomeTratado) > 0:
                    raise ValueError("Informe somente o primeiro nome - >")
            else:
                print("Nome recebido!")
                nomeTratado = novoNome
            novaSenha =  str(input("Informe a senha -  6 digitos somente de números -> "))
            if 6 <= len(novaSenha) <= 6:
                for i in novaSenha:
                    if i in "0123456789":
                        continue
                    else:
                        raise ValueError("ERRO DE COMPOSIÇÂO DE SENHA!")
            else:
                raise ValueError("ERRO DE COMPOSIÇÂO DE SENHA!")

            data = [(novoCod), (nomeTratado), (novaSenha), (novoScoreName)]
            fim = ObjEscreverCSV.escrevercsv(data, pegarDirRaiz)
            if fim == 1:
                raise ValueError("RETORNANDO!")
            else:
                raise ValueError("ERRO! - REINICIANDO!")

        except ValueError as e:
            print("LOG -> ", e)

        finally:
            return self.alert


ObjCriarProfile = CriarProfile()
