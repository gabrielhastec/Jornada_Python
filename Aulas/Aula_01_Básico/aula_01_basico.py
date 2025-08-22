"""
Aula 01 - Introdução ao Python
Autor: Gabriel Rodrigues
Descrição: Demonstra conceitos básicos de Python, incluindo impressão,
variáveis, tipos de dados, entrada de dados, conversões e verificação de tipos.
"""

# 1. Imprimir mensagens na tela
print("Olá, mundo!")
print("Estou aprendendo Python!\n")  # \n cria uma linha em branco

# 2. Criação de variáveis
# Variáveis armazenam dados. Podemos usar diferentes tipos de dados.
# Exemplo de variáveis com diferentes tipos de dados
# String, inteiro, float e booleano.

nome = "Gabriel"        # string (texto)
idade = 25              # inteiro (número inteiro)
altura = 1.78           # float (número com ponto flutuante)
estudando = True        # booleano # (verdadeiro ou falso)

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Está estudando?", estudando)

# 3. Convenção para constantes
# Constantes são valores que não mudam, geralmente escritas em letras maiúsculas.
PI = 3.14159  # por convenção, constantes usam letras maiúsculas
print("Valor de PI:", PI)

# 4. Exemplo de snake_case
## Snake case é uma convenção de nomenclatura onde as palavras são separadas por sublinhados.
meu_nome_completo = "Gabriel Rodrigues" 
idade_usuario = 25
print("Meu nome completo:", meu_nome_completo)
print("Idade do usuário:", idade_usuario)

# 5. Entrada de dados do usuário
nome_completo = input("Digite seu nome completo: ")  # Solicita o nome completo do usuário
print("Nome completo digitado:", nome_completo)

usuario = input("Digite seu nome: ") # Solicita o nome do usuário
print("Bem-vindo,", usuario) # Exibe uma mensagem de boas-vindas

idade_input = input("Digite sua idade: ") # Solicita a idade do usuário
print("Idade digitada:", idade_input)  # Exibe a idade digitada

# 6. Conversões de tipos

# String para inteiro
numero_str = "10"
numero_int = int(numero_str) # Converte string para inteiro
print(numero_str, "->", type(numero_str))   # Exibe o tipo original
print(numero_int, "->", type(numero_int))   # Exibe o tipo convertido

# Inteiro para float
numero_float = float(numero_int)   # Converte inteiro para float
print(numero_int, "->", type(numero_int))   # Exibe o tipo original
print(numero_float, "->", type(numero_float))  # Exibe o tipo convertido

# Float para string
altura_str = str(altura)    # Converte float para string
print(altura, "->", type(altura))   # Exibe o tipo original
print(altura_str, "->", type(altura_str))   # Exibe o tipo convertido

# Qualquer valor para booleano
print("Conversão de valores para booleano:")
print(bool(1))      # True (qualquer número diferente de zero é True)
print(bool(0))      # False (zero é False)
print(bool(""))     # False (string vazia é False)
print(bool("abc"))  # True (string não vazia é True)
print(bool([]))     # False (lista vazia é False)
print(bool([1, 2, 3]))  # True (lista não vazia é True)
print(bool(None))   # False (None é False)
print(bool(True))   # True (True é sempre True)
print(bool(False))  # False (False é sempre False)

# 7. Verificação de tipos
# Exibe o tipo de cada variável
print("Verificação de tipos:")  
print("Tipo de nome:", type(nome))  # Exibe o tipo da variável nome
print("Tipo de idade:", type(idade))  # Exibe o tipo da variável idade
print("Tipo de altura:", type(altura))  # Exibe o tipo da variável altura
print("Tipo de estudando:", type(estudando))  # Exibe o tipo da variável estudando  

# 8. Comentários
# Comentários são usados para explicar o código e não são executados.
# Este é um comentário de linha única
# Este é um comentário de múltiplas linhas
"""
Este é um comentário de múltiplas linhas.
Pode ser usado para descrever partes do código ou deixar notas.
"""
