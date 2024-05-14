import funcoes

nomes = ['Francisco', 'João', 'Maria', 'Ana', 'Sofia', 'Jéssica', 'Fabricio', 'Carlos']
apelidos = ['Ribeiro', 'Gonçalves', 'Carvalho', 'Fernandes', 'Mendes', 'Noval', 'Dantas', 'Pereira']

total_nomes = int(input('- Digita quantos nomes completos desejas criar: '))

for i in range(1, total_nomes+1):
    print(f'{i} - {funcoes.getNomesAleatorios(nomes, apelidos)}.')

print('\n')