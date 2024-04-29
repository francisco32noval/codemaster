import funcoes

funcoes.limpa()


frutas = ['uva', 'maça', 'morango', 'ananás', 'banana', 'laranja']

print(frutas)

print()

print(f'O primeiro elemento é: {frutas[0]}')

print()


print(f'Ultimo elemento, positivo: {frutas[len(frutas) - 1]}\n')


print()


print(f'Ultimo elemento, negativo: {frutas[-1]}\n')


print()

sublista = frutas[1:4]
print(f'Sublista do 2º ao 4º elemento: {sublista}\n')


print()

frutas[1] = 'clementinas'

print(frutas)






print('\n')