import funcoes
import os 
import time 

nome = input('- Indica o nome do(a) aluno(a): ')
n1 = float(input('- Indica a nota da primeira avaliação: '))
n2 = float(input('- Indica a nota da segunda avaliação: '))
n3 = float(input('- Indica a nota da terceira avaliação: '))

funcoes.limpar()

funcoes.analisar(0.3)


print(f'O(a) aluno(a) ({nome}) obteve uma media final de ({funcoes.getMediaFinal(n1, n2, n3):.2f}).')


print('\n')
