# Exercício 04 - Estruturas de Controle em Python
# Autor: Gabriel Rodrigues

# 1. Peça ao usuário um número e diga se ele é par ou ímpar.
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 2. Solicite uma nota e informe se o aluno está aprovado (>=7), em recuperação (>=5 e <7) ou reprovado (<5).
nota = float(input("Digite a nota do aluno: "))
if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")

# 3. Imprima os números de 1 a 10 usando um loop while.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# 4. Peça ao usuário um número e imprima a tabuada desse número de 1 a 10 usando for.
tabuada = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")

# 5. Dada uma lista de nomes, imprima apenas os nomes que começam com a letra 'A'.
nomes = ["Ana", "Bruno", "Amanda", "Carlos", "Alice"]
for nome in nomes:
    if nome.startswith("A"):
        print(nome)