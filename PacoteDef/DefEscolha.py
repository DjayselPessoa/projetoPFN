from PacoteEscolha.SobrePrograma import ObjSobrePrograma
from PacoteEscolha.OpAritmetico import ObjOpAritmetico
from PacoteEscolha.OpAssociacao import ObjOpAssociacao
from PacoteEscolha.OpAtribuicao import ObjOpAtribuicao
from PacoteEscolha.OpComparacao import ObjOpComparacao
from PacoteEscolha.OpIdentidade import ObjOpIdentidade
from PacoteEscolha.OpLogico import ObjOpLogico


class Escolha:

    def escolha(self, escolhaOp):
        self.escolhaOp = escolhaOp
        escolhaOp = self.escolhaOp
        sair = "ok"
        try:
            if escolhaOp == "1":
                ObjOpAritmetico.opAritmetico()
                return ""
            elif escolhaOp == "2":
                ObjOpAtribuicao.opAtribuicao()
                return ""
            elif escolhaOp == "3":
                ObjOpComparacao.opComparacao()
                return ""
            elif escolhaOp == "4":
                ObjOpLogico.oplogico()
                return ""
            elif escolhaOp == "5":
                ObjOpIdentidade.opIdentidade()
                return ""
            elif escolhaOp == "6":
                ObjOpAssociacao.opAssociacao()
                return ""
            elif escolhaOp == "7":
                ObjSobrePrograma.sobrePrograma()
                return ""
            elif escolhaOp == "8":
                print("\nDesligando!")
                return sair
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)


ObjEscolha = Escolha()