import funcoes

funcoes.limpa()


original = [['morango', 'banana', 'uva'], ['frango', 'bifana', 'novilho'], ['agua', 'cola', 'pepsi']]


print(original)

print()

print('==== FOR PARA CADA LISTA DENTRO DA MATRIZ ====\n')

for linha in original: print(linha)

print()

print('==== FOR PARA CADA ITEM DENTRO DE CADA LISTA ====\n')

for linha in original:
    for coluna in linha:
        print(coluna)
    print()



print('\n')