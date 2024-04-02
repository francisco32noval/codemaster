import funcoes

print('\n\n')

c = float(input('- Digite temperatura em celcius: '))
print()

escala = input('- Deseja converter para (K)elvin ou (F)erheneit: ')

print()

if(escala.lower() == 'k'): funcoes.calcularK(c)
elif(escala.lower() == 'f'): funcoes.calcularF(c)
else: print('----- Opção Inválida -----')