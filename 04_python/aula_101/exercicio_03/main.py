import funcoes

funcoes.limpa()


total_alunos = int(input('- Indica quantos alunos vão ser matriculados: '))
alunos = []

for i in range(total_alunos):
    alunos.append(input(f'Indica o nome do {i + 1}º aluno(a): '))


funcoes.limpa()

print('==== Lista de alunos ordenado ====\n')


for i in range(len(alunos)):
    print(f'{i + 1} - {alunos[i]}')


print('\n')