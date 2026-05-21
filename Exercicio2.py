#2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre 
#na tela os valores lidos.
vetor=[0,1,2,3,4,5]
for n in range(6):
    numeros=int(input(f"Digite o {n} número: "))
    vetor[n]=numeros

print(f"Valores lidos: {vetor}")