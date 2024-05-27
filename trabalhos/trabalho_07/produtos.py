
class Produto:


    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    

    # METODOS
    
    def toString(self, id) -> str:
        print(f"#{id + 1} - (Nome: {self.nome}) (Preço: {self.preco:.2f} €) (Quantidade: {self.quantidade})")
   


    def nomeJaExiste(self, novo_produto: str):
        return self.nome.lower() == novo_produto.lower()
    

    


    def setNome(self, novo_nome): self.nome = novo_nome

    def setPreco(self, novo_preco): self.preco = novo_preco
    
    def setQuantidade(self, nova_quantidade): self.quantidade = nova_quantidade