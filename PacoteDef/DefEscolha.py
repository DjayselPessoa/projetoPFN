from PacoteEscolha.SobrePrograma import ObjSobrePrograma
from PacoteEscolha.OpAritmetico import ObjOpAritmetico
from PacoteEscolha.OpAssociacao import ObjOpAssociacao
from PacoteEscolha.OpAtribuicao import ObjOpAtribuicao
from PacoteEscolha.OpComparacao import ObjOpComparacao
from PacoteEscolha.OpIdentidade import ObjOpIdentidade
from PacoteEscolha.OpLogico import ObjOpLogico


class Escolha:

    def escolha(self, escolhaOp, score, cod):
        self.escolhaOp = escolhaOp
        self.score = score
        self.cod = cod
        sair = "no"
        try:
            if self.escolhaOp == "1":
                self.score = ObjOpAritmetico.opAritmetico(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "2":
                self.score = ObjOpAtribuicao.opAtribuicao(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "3":
                self.score = ObjOpComparacao.opComparacao(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "4":
                self.score = ObjOpLogico.oplogico(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "5":
                self.score = ObjOpIdentidade.opIdentidade(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "6":
                self.score = ObjOpAssociacao.opAssociacao(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "7":
                self.score = ObjSobrePrograma.sobrePrograma(self.score)
                sair = "no"
                return sair, self.score, self.cod
            elif self.escolhaOp == "8":
                print("\nVOLTANDO")
                sair = "ok"
                return sair, self.score, self.cod

        except ValueError as e:
            print("\nLOG -> ", e)


ObjEscolha = Escolha()
