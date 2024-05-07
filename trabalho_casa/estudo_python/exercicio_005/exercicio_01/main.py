import funcoes

funcoes.limpa()

for i in range(10):
    print(i + 1)

print()

for i in range(9, -1, -1):
    print(i + 1)


print()

for i in range(101, 112):
    print(i)



print()

# valor = -1

# # Loop que continua até que um valor inteiro não negativo seja recebido
# while valor < 0:
#     entrada = int(input("Digite um valor inteiro não negativo: "))
#     if entrada < 0:
#         print("Por favor, digite um número maior ou igual a zero.")
#     else:
#         valor = entrada

# # Loop for para imprimir os números de 0 até o valor
# for i in range(valor + 1):
#     print(i)


print()

loop = 1

while(loop <= 10):
    print(f'8 * {loop} = {8 * loop}')
    loop += 1


print()

loop = 1
numero = int(input('- Digita um numero inteiro positivo: '))
while(loop <= 10):
    print(f'{numero} * {loop} = {numero * loop}')
    loop += 1


print('\n\n')