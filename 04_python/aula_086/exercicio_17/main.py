import funcoes
import os 
import time 

n1 = float(input('- Indica a nota da primeira avaliação: '))
n2 = float(input('- Indica a nota da segunda avaliação: '))

funcoes.limpar()

funcoes.analisar(0.3)

print(funcoes.getMedia(n1,n2))

print('\n')
