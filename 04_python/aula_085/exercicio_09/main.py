import funcoes
import os 
import time 


nome = input('- Indica o nome do funcionário: ')
salario_atual = float(input('- Indica o salário atual em euros e cêntimos (ex: 1210(euros).85(cêntimos)): '))
percentual_reajuste = float(input('- Indica o percentual de reajuste: '))

funcoes.limpar()

funcoes.analisar(0.3)

funcoes.limpar()

print(f'O novo salário do(a) ({nome}) é ({funcoes.calcularNovoSalario(salario_atual, percentual_reajuste):.2f}) euros.')

print('\n')
