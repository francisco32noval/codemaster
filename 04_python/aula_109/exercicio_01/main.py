import funcoes
from Login import *


funcoes.limpa()

l1 = Login('Fabricio', 'fabricio123', 'teste')
l2 = Login('Maria', 'maria7', 'code')
l3 = Login('Andre', 'andre_j', 'pet_123')

print('=== Lista Original ===\n')
l1.toString()
l2.toString()
l3.toString()
print()

aceder_login = input('- Indica qual login desejas encontrar: ')
print()

if(aceder_login.lower() == l1.login):
    l1.toString()
    print('\n--- Encontrado! ---')
elif(aceder_login.lower() == l2.login):
    l2.toString()
    print('\n--- Encontrado! ---')
elif(aceder_login.lower() == l3.login):
    l3.toString()
    print('\n--- Encontrado! ---')
else:
    print('--- Login Inválido! ---')



print('\n')