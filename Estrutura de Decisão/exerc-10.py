'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"
'''

M = ("Matutino")
V = ("Vespertino")
N = ("Noturno")

str(input("Qual o seu turno? "))

if turno == M:
    print("Bom dia!")
elif turno == V:
    print("Boa tarde!")
else turno == N:
    print("Boa noite!")