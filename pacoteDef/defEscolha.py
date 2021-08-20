from pacoteEscolha.sobrePrograma import sobrePrograma
from pacoteEscolha.opAritmetico import opAritimetico
from pacoteEscolha.opAssociacao import opAssociacao
from pacoteEscolha.opAtribuicao import opAtribuicao
from pacoteEscolha.opComparacao import opComparacao
from pacoteEscolha.opIdentidade import opIdentidade
from pacoteEscolha.oplogico import oplogico



def escolha(escolhaOp):
    sair = "ok"
    escolhaOp = escolhaOp
    try:
        if escolhaOp == "1":
            opAritimetico()
            return ""
        elif escolhaOp == "2":
            opAtribuicao()
            return ""
        elif escolhaOp == "3":
            opComparacao()
            return ""
        elif escolhaOp == "4":
            oplogico()
            return ""
        elif escolhaOp == "5":
            opIdentidade()
            return ""
        elif escolhaOp == "6":
            opAssociacao()
            return ""
        elif escolhaOp == "7":
            sobrePrograma()
            return ""
        elif escolhaOp == "8":
            print("\nDesligando!")
            return sair
        else:
            raise ValueError("\nInformação incorreta!")

    except ValueError as e:
        print("\nopção inexistente -", e)
