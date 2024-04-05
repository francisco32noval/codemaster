import funcoes

print('\n')

festa_agosto = funcoes.precoPorPessoa(150, 20)
festa_pda = funcoes.precoPorPessoa(200, 30)


var = float(input('- Qual é o preço total? '))
var2 = float(input('- Quantas pessoas são? '))

precofinal = funcoes.precoPorPessoa(var,var2)

print(f'cada pessoa paga {precofinal} ')



print(f'cada pessoa paga {funcoes.precoPorPessoa(float(input('- Qual é o preço total? ')), float(input('- Quantas pessoas são? ')))} ')


#print(funcoes.precoPorPessoa(float(input('- Qual é o preço total? ')), float(input('- Quantas pessoas são? '))))

#print(f'cada pessoa paga : ')



print('\n')