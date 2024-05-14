import funcoes
from Login import *


funcoes.limpa()

l1 = Pessoa('Fabricio', 'fabricio123', 'teste')
l2 = Pessoa('Maria', 'maria7', 'code')
l3 = Pessoa('Andre', 'andre_j', 'pet_123')

print('=== Lista Original ===\n')
l1.toString()
l2.toString()
l3.toString()
print()

opcao = input('- Indica qual login desejas encontrar: ')
print()

if(opcao.lower() == l1.login):
    l1.toString()
    print('\n--- Encontrado! ---')
elif(opcao.lower() == l2.login):
    l2.toString()
    print('\n--- Encontrado! ---')
elif(opcao.lower() == l3.login):
    l3.toString()
    print('\n--- Encontrado! ---')
else:
    print('--- Login Inválido! ---')


print('\n')