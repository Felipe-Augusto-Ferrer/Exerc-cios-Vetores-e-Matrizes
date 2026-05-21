#3. Ler um conjunto de números reais, armazenando-o em vetor e calcular
# o quadrado das componentes deste vetor, armazenando o resultado em 
# outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os 
# conjuntos


vetor1=[0,1,2,3,4,5,6,7,8,9]
vetor2=[0,1,2,3,4,5,6,7,8,9]
for n in range(10):
    numero=int(input("Digite um número: "))
    vetor1[n]=numero
    quadrado=vetor1[n]**2
    vetor2[n]=quadrado

print(f"Lista 1: {vetor1}")
print(f"Quadrado da lista 1: {vetor2}")
