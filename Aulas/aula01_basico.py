# Aula 01 - Introdução ao Python

# 1. Imprimir mensagens na tela
print("Olá, mundo!")
print("Estou aprendendo Python!\n")  # \n cria uma linha em branco

# 2. Criação de variáveis
nome = "Gabriel"        # string
idade = 25              # inteiro
altura = 1.78           # float
estudando = True        # booleano

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Está estudando?", estudando)

# 3. Convenção para constantes
PI = 3.14159  # por convenção, constantes usam letras maiúsculas
print("Valor de PI:", PI)
print("-" * 30)

# 4. Exemplo de snake_case
meu_nome_completo = "Gabriel Rodrigues"
idade_usuario = 25
print("Meu nome completo:", meu_nome_completo)
print("Idade do usuário:", idade_usuario)
print("-" * 30)

# 5. Entrada de dados do usuário
usuario = input("Digite seu nome: ")
print("Bem-vindo,", usuario)

idade_input = input("Digite sua idade: ")
print("Tipo antes da conversão:", type(idade_input))

# 6. Conversões de tipos

# String para inteiro
numero_str = "10"
numero_int = int(numero_str)
print(numero_str, "->", type(numero_str))
print(numero_int, "->", type(numero_int))

# Inteiro para float
numero_float = float(numero_int)
print(numero_float, "->", type(numero_float))

# Float para string
altura_str = str(altura)
print(altura_str, "->", type(altura_str))

# Qualquer valor para booleano
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("abc"))  # True
print(bool([]))     # False