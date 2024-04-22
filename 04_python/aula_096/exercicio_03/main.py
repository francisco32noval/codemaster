import time
import os
import funcoes


funcoes.limpar()

inicio = int(input('- Digita o valor inicial da tua lista: '))
fim = int(input('- Digita o valor final da tua lista: '))

for i in range(inicio, fim+1):
    print(i)

print('\n')