print('\n\n')

nome = input('- Digite o nome do aluno(a): ')
nota_1 = int(input('- Digite a nota da prova 1: '))
nota_2 = int(input('- Digite a nota da prova 2: '))
nota_tpc = int(input('- Digite a nota do trabalho de casa: '))

media = (nota_1 + nota_2 + nota_tpc) / 3

print()
print(f'O(a) aluno(a) obteve uma média final de ({(media):.1f}) valores')

print('\n\n')
