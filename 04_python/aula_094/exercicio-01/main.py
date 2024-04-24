import funtcion


funtcion.limpa()

print('==== Maior e menor numero ===')

total_numero = int(input('- Indica o total de numeros a serem analisados: '))

loop = 1
maior = None
menor = None

while(loop <= total_numero):

    numero = int(input(f'- Indica o ({loop}º) numero: '))
    if(loop == 1):
        maior = numero
        menor = numero
    else:
        if(numero > maior): maior = numero
        if(numero < menor): menor = numero
    loop += 1



print(f'Maior ({maior})')
print(f'Menor ({menor})')

print('\n')