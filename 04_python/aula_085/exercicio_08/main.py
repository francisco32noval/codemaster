import funcoes
import os 
import time 


municipio = input('Indica o nome do municipio: ')
total_eleitores = int(input('- Indica o total de eleitores: '))
brancos = int(input('- Digite o total de votos brancos: '))
nulos = int(input('- Digite o total de votos nulos: '))
validos = int(input('- Digite o total de votos válidos: '))

funcoes.limpar()

funcoes.analisar(0.3)

print(f'O Municipio do(a) ({municipio}) tem ({total_eleitores}) eleitores.\n')

print(f'Nas eleições o Municipio ({municipio}) teve ({funcoes.percentual(brancos, total_eleitores):.2f}%) de votos brancos.\n')

print(f'Nas eleições o Municipio ({municipio}) teve ({funcoes.percentual(nulos, total_eleitores):.2f}%) de votos nulos.\n')

print(f'Nas eleições o Municipio ({municipio}) teve ({funcoes.percentual(validos, total_eleitores):.2f}%) de votos válidos.\n')
