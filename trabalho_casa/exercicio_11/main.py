import funcoes
import os 
import time 


nome = input('- Digita o nome do funcionário(a): ')
salario_fixo = float(input('- Indica o salário fixo: '))
valor_total_vendas = float(input('- Indica o valor total das vendas: '))
carros_vendidos = int(input('- Indica quantos carros vendeu este mês: '))
valor_por_carro = float(input('- Indica o valor recebido por carro: '))

funcoes.limpar()

funcoes.analisar(0.3)

print(f'O salário do(a) funcionário(a) ({nome}) será de ({funcoes.getSalario(salario_fixo, valor_total_vendas, carros_vendidos, valor_por_carro):.2f}).')

print('\n')
