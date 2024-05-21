from produto import *

class Loja:

    def __init__(self):
        self.produtos: list[Produto] = []


    def adicionar(self, produto_a_adicionar: Produto) -> bool:
        # 1. verificar se o produto ja existe
        for produto_existente in self.produtos:
            if produto_existente.nome == produto_a_adicionar.nome:
                return False

        # 2. adicionar o produto se existir
        self.produtos.append(produto_a_adicionar)
        return True
    

    def listar(self) -> dict[int, Produto]:
        pass

    def apagar(self, id: int) -> bool:
        pass
