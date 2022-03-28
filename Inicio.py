from pathlib import Path
from Core.AbrirCSV import ObjAbrirSCORE
from LayerMain import ObjLayerMain
from Core.Entrar import ObjEntrar
from Core.AbrirCSV import ObjAbrirCSV
from Data.CriarProfile import ObjCriarProfile
from Data.UpdateScore import ObjUpdateScore
from Core.RankScore import ObjRankScore
from csv import writer
from csv import QUOTE_MINIMAL
from time import sleep
import os


active = True

while active:
    try:
        os.chdir(os.path.dirname(__file__))
        pegarDirRaiz = str(os.getcwd())
        # -------------------------------------------------------------------------------------------------
        # Acima obtem-se o link do diretório atual do programa até este arquivo início.py
        # print("Ok1 ", pegarDirRaiz)
        # -------------------------------------------------------------------------------------------------
        alert = 0  # variável do primeiro uso
        # -------------------------------------------------------------------------------------------------
        # listas de controle e dados abaixo:
        # -------------------------------------------------------------------------------------------------
        cod = []
        nome = []
        senha = []
        scorename = []
        # -------------------------------------------------------------------------------------------------
        alert, cod, nome, senha, scorename = ObjAbrirCSV.abrircsv(pegarDirRaiz)  # abrindo e retornando conteúdo!
        # -------------------------------------------------------------------------------------------------
        # quando não tem nenhum usuário exibe mensagem de boas vindas
        # print("alert 2: ", alert)
        # -------------------------------------------------------------------------------------------------
        if alert == 0:
            print("Olá! Seja bem vindo ao PYTHON FOR NOOBS!")
            print("Já que esta é a sua primeira entrada")
            print("você precisará criar um profile: -> ")
            alert = ObjCriarProfile.criarprofile(alert, pegarDirRaiz)
            print("GERANDO SCOREFILE!")
            sleep(1)
            novoCod = "#"+str(alert + 1)
            novoScore = 0

            nomeArquivoSCORE = "score_"+novoCod+".csv"
            pathTratado = str(pegarDirRaiz)
            home = Path(pathTratado)
            sourcePath = Path(home, "Data", nomeArquivoSCORE)

            with open(sourcePath, 'w+', newline='') as csvfile:
                filewriter = writer(csvfile, quotechar='|', quoting=QUOTE_MINIMAL)
                filewriter.writerow(['SCORE'])
                filewriter.writerow([novoScore])
            csvfile.close()

        # -------------------------------------------------------------------------------------------------
        # Quando detectado ao menos um usuário o menu é mostrado
        # -------------------------------------------------------------------------------------------------
        elif len(cod) != 0 or alert == 1:
            print("\nBem vindo ao PYTHON FOR NOOBS!\n\nUtilize as letras iniciais para acessar: ->\n")
            listaExibir = ["Entrar", "Criar", "Sair", "Rank", "[E]", "[C]", "[S]", "[R]"]
            for i in range(4):
                print("{:<7s}{:^7s}".format(listaExibir[i], listaExibir[i + 4]))
            entrarCriar = (str(input(": -> "))).lower()

        if entrarCriar in "Cc":
            print("\nIniciando Criação: -> ")
            sleep(1)
            alert = ObjCriarProfile.criarprofile(alert, pegarDirRaiz)
            novoCod = "#"+str(alert + 1)
            novoScore = 0

            nomeArquivoSCORE = "score_"+novoCod+".csv"
            pathTratado = str(pegarDirRaiz)
            home = Path(pathTratado)
            sourcePath = Path(home, "Data", nomeArquivoSCORE)

            with open(sourcePath, 'w+', newline='') as csvfile:
                filewriter = writer(csvfile, quotechar='|', quoting=QUOTE_MINIMAL)
                filewriter.writerow(['SCORE'])
                filewriter.writerow([novoScore])
            csvfile.close()

            raise ValueError("\nREINICIANDO!")

        elif entrarCriar in "Ee":
            sleep(1)
            confirmar, position = ObjEntrar.entrar(nome, senha)
            if confirmar == 1:
                showName = nome[position].capitalize()
                sleep(1)
                print(f"\nSua entrada foi permitida! Bem vindo {showName}!\n")
                sleep(2)
                nomeUser = nome[position]
                # print(nomeUser)
                scoreUser = ObjAbrirSCORE.abrirScore(pegarDirRaiz, position, cod)
                positionScore = len(scoreUser) - 1
                scoreLido = int(scoreUser[positionScore])
                # print(scoreLido)
                codUser = cod[position]
                # print(codUser)
                active, scoreUserFinal, codUserFinal = ObjLayerMain.layermain(nomeUser, scoreLido, codUser, active)
                # print(scoreUserFinal)
                if active is False:
                    active = True
                    active = ObjUpdateScore.updatescore(scoreUserFinal, codUserFinal, active, pegarDirRaiz)
                    sleep(1)
                    raise ValueError("\nLOADING -> ")
            elif confirmar == 0:
                sleep(1)
                raise ValueError("\nLOADING -> ")

        elif entrarCriar in "Ss":
            sleep(1)
            print("\nFINALIZANDO APLICAÇÃO!")

            active = False
            sleep(1)
            raise ValueError("\nDESLIGANDO!")

        elif entrarCriar in "Rr":
            print(f"cod: {cod}")
            ObjRankScore.rankscore(pegarDirRaiz, cod, nome, active)
            sleep(1)
            ValueError("\nLOADING - > ")

    except ValueError as e:
        print("\nLOG: ->", e)
    finally:
        continue
