import funcoes
import os 
import time 
import math

print('\n')

funcoes.limpar()

print('===== Calculo de Áreas com funções =====\n')

print('--- Escolha uma opção ---\n')

print('(t) para triangulos')
print('(r) para retangulos')
print('(c) para circulos')

opcao = input('Opção: ')

funcoes.limpar()

funcoes.analisar(0.3)

if(opcao.lower() == 't' or opcao.lower() == 'r' or opcao.lower() == 'c'):
    if(opcao.lower() == 't'):
        print(funcoes.getTriangulo())
    elif(opcao.lower() == 'r'):
        print(funcoes.getRetangulo())
    else:
        print(funcoes.getCirculo())
else:
    print('Erro! Opção Inválida')



print('\n')
