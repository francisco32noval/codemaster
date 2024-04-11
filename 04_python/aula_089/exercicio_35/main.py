import funcoes
import os 
import time 



combustivel = input('- Insira o tipo de combustivel: ')
quantidade = float(input('- Indica o total de litros: '))


funcoes.limpar()

funcoes.analisar(0.3)

print(f'O(a cliente tem a pagar um total de ({funcoes.getTotal(combustivel, quantidade)}))')



print('\n')
