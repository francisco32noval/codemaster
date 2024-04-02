print('\n\n')

print('=== Métodos e funções das Strings ===')

original = 'CodeMaster'
capitalizada = original.capitalize()
minuscula = original.lower()
maiuscula = original.upper()

total_letra_e = original.count('e')
total_letrasf = len(original)
total_letrasm = original.__len__()

substituir = original.replace('e', 'x')

print('Strin "original": (' + original + ')')
print('\n')

print('String "capitalizada": (' + original.capitalize() + ')')
print('String "minuscula": (' + original.lower() + ')')
print('String "maiuscula": (' + original.upper() + ')')
print('\n')


print('String "total de letras e": (' + str(original.count('e')) + ')')
print('String "tamanho total com metodo": (' + str(total_letrasm) + ')')
print('String "tamanho total com função": (' + str(total_letrasf) + ')')
print('\n')


print('String "capitalizada": (' + original.replace('e', 'x') + ')')

print('\n\n')
