print('\n\n')

nome = 'Francisco Noval'
n1 = 18.0
n2 = 13.0
nt = 16.0
media = (n1 + n2 + nt) / 3

print('=== Método "format" ===\n')

print('O(a) aluno(a) [{}] com as notas [n1: {}] [n2: {}] [nt: {}], obteve uma média de [{}]\n'.format(nome, n1, n2, nt, round(media, 1)))

print('O(a) aluno(a) [{4}] com as notas [n1: {2}] [n2: {0}] [nt: {1}], obteve uma média de [{3}]'.format(nome, n1, n2, nt, round(media, 1)))

print(f'O(a) aluno(a) [{nome}] com as notas [n1: {n1}] [n2: {n2}] [nt: {nt}], obteve uma média de [{round(media, 1)}]')