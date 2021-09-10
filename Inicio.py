from pathlib import Path
from Core.AbrirCSV import ObjAbrirSCORE
from LayerMain import ObjLayerMain
from Core.Entrar import ObjEntrar
from Core.AbrirCSV import ObjAbrirCSV
from Data.CriarProfile import ObjCriarProfile
from Data.UpdateScore import ObjUpdateScore
from csv import writer
from csv import QUOTE_MINIMAL
import os


active = True

while active:
    try:
        os.chdir(os.path.dirname(__file__))
        pegarDirRaiz = str(os.getcwd())
        # print("Ok1 ", pegarDirRaiz)
        alert = 0
        cod = []
        nome = []
        senha = []
        scorename = []
        alert, cod, nome, senha, scorename = ObjAbrirCSV.abrircsv(pegarDirRaiz)  # abrindo e retornando conteúdo!
        # print("alert 2", alert)
        if alert == 0:
            print("Olá! Seja bem vindo ao PYTHON FOR NOOBS!")
            print("Sendo esta a sua primeira entrada")
            print("você precisará criar um profile: -> ")
            alert = ObjCriarProfile.criarprofile(alert, pegarDirRaiz)
            print("GERANDO SCOREFILE!")
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

        elif len(cod) != 0 or alert == 1:
            entrarCriar = (str(input("Entrar - Criar - Sair -> "))).lower()

        if entrarCriar in "criar":
            print("Iniciando Criação: -> ")
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

            raise ValueError("REINICIANDO!")

        elif entrarCriar in "entrar":
            confirmar, position = ObjEntrar.entrar(nome, senha)
            if confirmar == 1:
                print("Sua entrada foi permitida! Seja bem vindo!")
                nomeUser = nome[position]
                # print(nomeUser)
                scoreUser = ObjAbrirSCORE.abrirScore(alert, pegarDirRaiz)
                positionScore = len(scoreUser) - 1
                scoreLido = int(scoreUser[positionScore])
                # print(scoreLido)
                codUser = cod[position]
                # print(codUser)
                active, scoreUserFinal, codUserFinal = ObjLayerMain.layermain(nomeUser, scoreLido, codUser, active)
                # print(scoreUserFinal)
                if active == False:
                    active = ObjUpdateScore.updatescore(scoreUserFinal, codUserFinal, active, pegarDirRaiz)
                    raise ValueError("SAINDO!")
            elif confirmar == 0:
                raise ValueError("LOADING -> ")

        elif entrarCriar in "sair":
            print("Seus dados estão salvos!")

            active = False
            raise ValueError("DESLIGANDO!")
        else:
            raise ValueError("DADO INCORRETO! REINICIANDO")

    except ValueError as e:
        raise ValueError("LOG: ->", e)
    finally:
        continue
