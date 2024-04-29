import funcoes

funcoes.limpa()


frutas = ['uva', 'maça', 'morango']

print(frutas)

print()

print('Adicionar ananás\n')
frutas.append('ananás')
print(frutas)

print()

print('Laranja na segunda posição\n')
frutas.insert(1, 'laranja')
print(frutas)

print()

print('Remover primeiro elemento\n')
frutas.pop(0)
print(frutas)

print()

print('Remover morango\n')
frutas.remove('morango')
print(frutas)


print('\n')