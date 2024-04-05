import funcoes

base = float(input('- Indica a base do retângulo: '))
altura = float(input('- Indica a altura do retângulo: '))


funcoes.limpar()

print(f'A área do teu retângulo é ({funcoes.getAreaRetangulo(base,altura)})')