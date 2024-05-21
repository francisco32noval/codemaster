class Produto:


    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    

    # METODOS
    
    def to_string(self) -> str:
        return f"(Nome: {self.nome}) (Preço: {self.preco:.2f}€) (Quantidade: {self.quantidade})"
    """
    def equals(self, other_product)
        return self.nome.lower() != other_product.lower()
    """