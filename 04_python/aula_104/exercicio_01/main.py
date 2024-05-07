import funcoes

funcoes.limpa()


dicionario = {
    'nome' : 'Francisco Noval',
    'idade' : 24,
    'morada' : 'Fafe'
}

print(dicionario)

print()

print('==== DICIONARIO COM FOR ====\n')

for i in dicionario:
    print(f'{i}: {dicionario[i]}')


print()

print('==== DICIONARIO APENAS CHAVES ====')

for i in dicionario.keys():
    print(i)


print()

print('==== DICIONARIO APENAS CHAVES ====')

for i in dicionario.values():
    print(i)

print('\n')