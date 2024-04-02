print('\n\n')

nome = input('- Digite o nome do(a) paciente: ')
peso = float(input('- Digite o peso do(a) paciente (Kg): '))
altura = float(input('- Digite a altura do(a) paciente (m): '))

imc = peso / altura ** 2

print()

print(f'O(a) paciente ({nome}) está com o IMC de ({imc:.1f})')

print('\n\n')
