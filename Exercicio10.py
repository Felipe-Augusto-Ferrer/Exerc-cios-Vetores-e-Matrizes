#Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
#e imprima a média geral.


notaTotal=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
total=0
for aluno in range(15):
    nota=int(input(f"Digite a nota do aluno {aluno}: "))
    notaTotal[aluno]=nota
    total+=nota

media=total/15
print(f"Nota de todos os alunos: {notaTotal}")
print(f"A média da sala é : {media:.2f}")
