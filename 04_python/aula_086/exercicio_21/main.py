import funcoes
import os 
import time 


hora_inicio = int(input('- Indica a hora de inicio da partida: '))
hora_fim = int(input('- Indica a hora de término da partida: '))


funcoes.limpar()

funcoes.analisar(0.3)


print(f'A partida teve um total de ({funcoes.getHorasJogo(hora_fim, hora_inicio)}) horas.')


print('\n')
