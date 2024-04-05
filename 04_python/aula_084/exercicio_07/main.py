import funcoes
import os

anos = int(input('- Indica o total de anos que tem: '))
meses = int(input('- Indica o total de meses que tem: '))
dias = int(input('- Indica o total de dias que tem: '))


funcoes.limpar()

print(f'Voce tem ({funcoes.getAnosEmDias(anos, meses, dias)}) dias de vida')

print('\n')

