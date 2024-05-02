import funcoes

funcoes.limpa()


frutas = ['uva', 'maça', 'morango', 'ananás', 'banana', 'laranja']

padaria = ['bolo', 'pão', 'queijo']

print(frutas)
print(padaria)

print()

frutas.sort()
print(f'Lista de frutas ordenada: {frutas}')


print()

frutas.sort(reverse=True)
print(f'Lista de frutas ordenada reversa: {frutas}')

print()

if('morango' in frutas): print('morango está na lista 1.\n')
else: print('Falso\n')

print('-' *20)

frutas.extend(padaria)
print(f'Lista 1 extendida com a lista 2.\n{frutas}\n')

print('-' *20)

frutas.clear()
    
print(f'Lista 1 limpada: {frutas}')


print('\n')