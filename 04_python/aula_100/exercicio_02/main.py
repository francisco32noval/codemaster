import funcoes

funcoes.limpa()


frutas = ['uva', 'maça', 'morango', 'ananás', 'banana', 'laranja']

print(frutas)

print()

print('==== Lista de frutas com FOR ====\n')

for f in frutas:
    print(f)


print()


print()

print('==== Lista de frutas com FOR + RANGE ====\n')

for i in range(len(frutas)):
    print(f'{i + 1} - {frutas[i]}')


print()


print('==== Lista de frutas com FOR + REVERSE ====\n')

for f in reversed(frutas): print(f)


print()

print('==== Lista de frutas com FOR + RANGE + REVERSE ====\n')

for i in range(len(frutas)-1, -1, -1):
    print(f'{i + 1} - {frutas[i]}')






print('\n')