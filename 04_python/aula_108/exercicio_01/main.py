import funcoes
from Pessoa import *


funcoes.limpa()



p1 = Pessoa('Fabricio Vidal', 28, 'Covilhã', 111)
p2 = Pessoa('Maria Silva', 54, 'Almada', 222)
p3 = Pessoa('Carlos Eduardo', 17, 'Porto', 333)
p4 = Pessoa('Manel Sousa', 66, 'Lisboa', 444)
p5 = Pessoa('Pedro Carvalho', 28, 'Amadora', 555)

print('=== Lista Original ===')
p1.toString()
p2.toString()
p3.toString()
p4.toString()
p5.toString()

print()

p1.fazerAnos()
p3.fazerAnos()
p5.fazerAnos()

print()

p2.mudarMorada('Braga')
p4.mudarMorada('Nazaré')


print()

print('=== Lista Final ===')
p1.toString()
p2.toString()
p3.toString()
p4.toString()
p5.toString()
print('\n')