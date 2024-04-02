import random
import math

print('\n\n')


n = -10
n_abs = abs(n)
aleatorio = random.randint(1, 5)

original = 3.567
arredondado = round(original)
arredondado_1 = round(original, 1)
arredondado_2 = round(original, 2)

arredondado_cima = math.ceil(original)
arredondado_baixo = math.floor(original)

print('=== Funções dos inteiros ===')


print('Inteiro "original": (' + str(n) + ')')
print('Inteiro "original": (' + str(n_abs) + ')\n')
print('Numero inteiro aleatório entre "1 e 5": (' + str(aleatorio) + ')')
print('\n')



print('=== Funções dos Floats ===\n')


print('Float "original": (' + str(original) + ')\n')
print('Float "arredondado": (' + str(arredondado) + ')')
print('Float "arredondado para 1 casa decimal": (' + str(arredondado_1) + ')')
print('Float "arredondado para 1 casa decimal": (' + str(arredondado_2) + ')\n')

print('Float "arredondado para cima": (' + str(arredondado_cima) + ')')
print('Float "arredondado para baixo": (' + str(arredondado_baixo) + ')')

print('\n\n')

