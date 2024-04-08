import funcoes
import os 
import time 

macas = int(input('- Indica quantas maças comprou: '))

funcoes.limpar()

funcoes.analisar(0.3)

print(f'As ({macas}) maças dão um total de ({funcoes.getValor(macas):.2f}).')

print('\n')
