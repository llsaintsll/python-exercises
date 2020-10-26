# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))

if n1>n2:
    print("O maior número é o primeiro!")
elif n1<n2:
    print("O maior número é o segundo!")
else:
    print("Os números são iguais!")