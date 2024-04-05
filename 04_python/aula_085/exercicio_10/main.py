import funcoes
import os 
import time 


custo_fabrica = float(input('- Digita o valor de fábrica do carro em euros e cêntimos (ex: 25245(euros).84(cêntimos)): '))
distribuidor_impostos = 0.73

funcoes.limpar()

funcoes.analisar(0.3)

funcoes.limpar()

print(f'O custo final ao consumidor é de ({funcoes.getValorConsumidor(custo_fabrica):.2f}) euros.')

print('\n')
