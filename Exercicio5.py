#Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
vetor = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    n = int(input("Digite um número: "))
    vetor[i]=n
print()

par = 0
for n in range(10):
    if vetor[n]%2==0:
        par += 1
print(f"números pares:{par}")        
