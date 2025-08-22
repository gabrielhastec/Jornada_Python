# Exercicio_02.py
# Exercício de fixação - Aula 02: Trabalhando com Texto (Strings)
# Autor: Gabriel Rodrigues

print("=== Exercício 02 - Strings ===\n")

# 1. Solicitar nome e sobrenome do usuário e mostrar a concatenação
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

# 2. Criar uma linha decorativa usando repetição
linha = "=" * 30
print("Linha decorativa:", linha)

# 3. Solicitar uma frase e mostrar indexação
frase = input("Digite uma frase: ")
print("Primeiro caractere:", frase[0])
print("Último caractere:", frase[-1])
print("Terceiro caractere:", frase[2])
print("Quinto caractere:", frase[4])

# 4. Mostrar fatiamento da frase
print("Primeiros 3 caracteres:", frase[0:3])
print("Últimos 3 caracteres:", frase[-3:])

# 5. Quebra de linha e tabulação
print("Exemplo de quebra de linha:\nLinha 1\nLinha 2")
print("Exemplo de tabulação:\tColuna 1\tColuna 2")

# 6. Aplicar métodos de string
print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Título:", frase.title())
print("Primeira letra maiúscula:", frase.capitalize())
print("Inverter casos:", frase.swapcase())
print("Comprimento da frase:", len(frase))
print("Dividir em palavras:", frase.split())
print("Começa com 'Python'?", frase.startswith("Python"))
print("Termina com 'legal'?", frase.endswith("legal"))
print("Só letras?", frase.isalpha())
print("Só letras e números?", frase.isalnum())
print("Só dígitos?", frase.isdigit())
print("Só espaços?", frase.isspace())
print("Remover espaços extras:", frase.strip())
print("Substituir espaços por '_':", frase.replace(" ", "_"))
print("Contar 'a':", frase.lower().count("a"))

# 7. Exemplo de f-string
idade = int(input("Digite sua idade: "))
print(f"Meu nome é {nome_completo} e tenho {idade} anos.")
