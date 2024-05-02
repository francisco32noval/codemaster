import funcoes

funcoes.limpa()


original = [['Fabricio', 28, 'coviha'], ['Francisco', 24, 'Fafe'], ['Jao', 32, 'porto'], ['ana', 56, 'amadora']]


print(original)

print()

print('==== Lista das pessoas na matriz ====\n')

for p in original:
    print(f'{p[0]} - (Idade: {p[1]}) - (Morada: {p[2]})')



print('\n')