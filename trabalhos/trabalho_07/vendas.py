import globals
@classmethod
def valorTotalVendas(cls):
    valor_vendas = sum(venda.calcularVenda() for venda in globals.total_vendas)
    return valor_vendas

class Venda:

    def __init__(self, nome: str, preco: float, quantidade_vendida: int):
        self.nome = nome
        self.preco = preco
        self.quantidade_vendida = quantidade_vendida

    def toStringVenda(self, id) -> str:
        total = self.preco * self.quantidade_vendida
        print(f"Venda #{id + 1} - {self.nome} ({self.preco:.2f} €) * ({self.quantidade_vendida} uni.) = ({total:.2f} €)")
        

    
    
    def calcularVenda(self):
        return self.preco * self.quantidade_vendida


    # Metodo responsável por dar acesso á classe e poder operar sobre a mesma 
    @classmethod
    def valorTotalVendas(cls):
        valor_vendas = sum(venda.calcularVenda() for venda in globals.total_vendas)
        return valor_vendas

