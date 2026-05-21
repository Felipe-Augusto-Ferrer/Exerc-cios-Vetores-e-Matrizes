#Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
#juntamente com o maior, o menor e a média dos valores.

vetor=[0,1,2,3,4]
soma = 0
for i in range(5):
    n=int(input("Digite um número:"))
    vetor[i]= n
    soma += n
print()
print(vetor)
print(f"Valor máximo: {max(vetor)}")
print(f"Valor mínimo: {min(vetor)}")
print(f"Soma: {soma}")
