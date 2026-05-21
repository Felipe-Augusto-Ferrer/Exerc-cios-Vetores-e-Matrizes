#Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
#na ordem inversa.
vetor = [0,1,2,3,4,5]
for i in range(6):
    n = int(input("Digite um número: "))
    vetor[i]= n
vetor.reverse()
print(vetor)