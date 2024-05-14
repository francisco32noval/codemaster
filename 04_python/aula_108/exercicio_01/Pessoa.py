class Pessoa:

    def __init__(self, nome, idade, morada, nif):
        self.nome = nome
        self.idade = idade
        self.morada = morada
        self.nif = nif

    def toString(self):
        print(f'{self.nome} -> (Idade: {self.idade}) - (Morada: {self.morada}) (NIF: {self.nif})')

    def fazerAnos(self):
        print(f'{self.nome} fez anos!')
        self.idade += 1

    def mudarMorada(self, nova_morada):
        print(f'{self.nome} modou de morada ({self.morada} -> {nova_morada})')
        self.morada = nova_morada