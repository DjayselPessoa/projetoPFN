from Inicio import ObjInicio
from Core.Entrar import ObjEntrar
from Core.AbrirCSV import ObjAbrirCSV
from Data.CriarProfile import ObjCriarProfile

active = True

while active:
    try:

        alert = 0
        cod = []
        nome = []
        senha = []
        score = []

        alert, cod, nome, senha, score = ObjAbrirCSV.abrircsv() # abrindo e retornando conteúdo!

        if alert == 0:
            print("Você precisa criar um profile -> ")
            alert = ObjCriarProfile.criarprofile(alert)
        elif len(cod) != 0 or alert == 1:
            entrarCriar = (str(input("Entrar - Criar - Sair -> "))).lower()

        if entrarCriar in "criar":
            print("Iniciando Criação: -> ")
            alert = ObjCriarProfile.criarprofile(alert)
            raise ValueError("REINICIANDO!")



        elif entrarCriar in "entrar":
            confirmar, position = ObjEntrar.entrar(nome, senha)
            if confirmar == 1:
                print("Sua entrada foi permitida! Seja bem vindo!")
                nomeUser = nome[position - 1]
                print(nomeUser)
                scoreUser = score[position - 1]
                print(scoreUser)
                active = ObjInicio.inicio(nomeUser, scoreUser, active)
                if active == False:
                    raise ValueError("SAINDO!")

        elif entrarCriar in "sair":
            print("Seus dados estão salvos!")

            active = False
            raise ValueError("DESLIGANDO!")

    except ValueError as e:
        raise ValueError("LOG: ->", e)
    finally:
        continue
