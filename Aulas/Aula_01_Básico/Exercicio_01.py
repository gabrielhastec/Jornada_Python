"""
Exercício 01 – Fixação da Aula 01
Autor: Gabriel Rodrigues
Objetivo: Praticar variáveis, tipos de dados, entrada de usuário, conversão e impressão.
"""

# 1️⃣ Criação de variáveis
nome = "Gabriel"        # string
idade = 25              # inteiro
altura = 1.78           # float
estudando = True        # booleano

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Está estudando?", estudando)
print()  # linha em branco

# 2️⃣ Solicitar informações do usuário
nome_completo = input("Digite seu nome completo: ")  # entrada de string
idade_input = input("Digite sua idade: ")            # entrada de string

# 3️⃣ Conversão de tipos
idade_input_int = int(idade_input)  # converter string para inteiro

print("Nome completo digitado:", nome_completo)
print("Idade digitada convertida para inteiro:", idade_input_int)
print()  # linha em branco

# 4️⃣ Constante
PI = 3.14
print("Valor da constante PI:", PI)
print()  # linha em branco

# 5️⃣ Conversão de tipos
altura_str = str(altura)  # float para string
print("Altura original:", altura, "Tipo:", type(altura))
print("Altura convertida para string:", altura_str, "Tipo:", type(altura_str))
print()  # linha em branco

# 6️⃣ Conversão para booleano
print("Conversão de valores para booleano:")
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool('Python'):", bool("Python"))
print("bool(''):", bool(""))
print()  # linha em branco

# 7️⃣ Verificação de tipos
print("Tipos das variáveis:")
print("Tipo de nome:", type(nome))
print("Tipo de idade:", type(idade))
print("Tipo de altura:", type(altura))
print("Tipo de estudando:", type(estudando))
print("Tipo de idade_input_int:", type(idade_input_int))
print("Tipo de altura_str:", type(altura_str))
