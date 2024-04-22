import time
import os
import funcoes


funcoes.limpar()

inicio = int(input('- Digita o valor inicial da tua lista: '))
fim = int(input('- Digita o valor final da tua lista: '))
total_listas = int(input('- Quantas vezes deseja exibir esta lista numerica: '))

print()


for i in range(total_listas):
    print('---------------')

    for j in range(inicio, fim+1):
        print (j)



print('\n')