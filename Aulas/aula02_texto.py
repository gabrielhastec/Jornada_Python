# Aula 02 - Trabalhando com Texto (Strings)
# Nesta aula, vamos explorar como manipular textos em Python usando strings.

# 1. Concatenação de strings
# O operador + junta (concatena) dois ou mais textos em uma única string.
# Aqui, combinamos nome e sobrenome com um espaço entre eles.
nome = input("Digite seu nome: ")  # Solicita o nome do usuário
sobrenome = input("Digite seu sobrenome: ")  # Solicita o sobrenome
nome_completo = nome + " " + sobrenome  # Junta com um espaço
print("1. Concatenação de strings:")
print("   - Nome completo:", nome_completo)  # Exibe o resultado

# 2. Repetição de strings
# O operador * repete uma string o número de vezes indicado.
# Aqui, criamos uma linha decorativa repetindo o caractere "=".
linha = "=" * 20  # Repete "=" 20 vezes para criar uma linha visual
print("2. Repetição de strings:")
print("   - Linha decorativa:", linha)  # Útil para separar informações no terminal

# 3. Indexação
# Strings são como listas de caracteres, e cada caractere tem um índice (começa em 0).
# Usamos [índice] para acessar um caractere específico.
# Exemplo: em "Python", P está no índice 0, y no 1, etc.
frase = input("Digite uma frase (ex.: 'Python é legal'): ")  # Solicita uma frase
if frase:  # Verifica se a frase não está vazia para evitar erros
    primeiro_caractere = frase[0]  # Pega o primeiro caractere
    ultimo_caractere = frase[-1]  # Pega o último caractere (índice -1 conta do final)
    print("3. Indexação:")
    print("   - Primeiro caractere (frase[0]):", primeiro_caractere)
    print("   - Último caractere (frase[-1]):", ultimo_caractere)
else:
    print("3. Indexação: A frase está vazia!")

# 4. Fatiamento
# Fatiamento extrai uma parte da string usando [início:fim].
# O índice 'fim' não é incluído. Exemplo: "Python"[0:3] pega "Pyt" (índices 0, 1, 2).
primeiros_tres = frase[0:3]  # Pega os 3 primeiros caracteres
ultimos_tres = frase[-3:]  # Pega os 3 últimos caracteres
print("4. Fatiamento:")
print("   - Primeiros 3 caracteres (frase[0:3]):", primeiros_tres)  # Exibe os 3 primeiros
print("   - Últimos 3 caracteres (frase[-3:]):", ultimos_tres)  # Exibe os 3 últimos

# 5. Quebra de linha (\n) e tabulação (\t)
# \n insere uma nova linha, como pressionar Enter.
# \t insere uma tabulação, como pressionar Tab, para alinhar texto.
print("5. Quebra de linha e tabulação:")
print("   - Exemplo com \\n:\nLinha 1\nLinha 2")  # Demonstra quebra de linha
print("   - Exemplo com \\t:Coluna 1\tColuna 2")  # Demonstra tabulação

# 6. Métodos úteis de strings
# Métodos são funções que manipulam strings de formas específicas.

# Aqui, aplicamos vários métodos de transformação na frase fornecida pelo usuário.
print("6. Métodos úteis de strings:")
print("   - .upper(): Converte para maiúsculas:", frase.upper())  # Tudo maiúsculo
print("   - .lower(): Converte para minúsculas:", frase.lower())  # Tudo minúsculo
print("   - .title(): Primeira letra de cada palavra em maiúscula:", frase.title())  # Formato título
print("   - .capitalize(): Primeira letra maiúscula:", frase.capitalize())  # Primeira letra maiúscula
print("   - .swapcase(): Inverte maiúsculas e minúsculas:", frase.swapcase())  # Inverte casos

# Aqui, aplicamos vários métodos de análise na frase fornecida pelo usuário.
print("   - .len(): Comprimento da frase:", len(frase))  # Conta caracteres
print("   - .split(): Divide a frase em palavras:", frase.split())  # Divide em palavras
print("   - .startswith('Python'): Verifica se começa com 'Python':", frase.startswith("Python"))
print("   - .endswith('legal'): Verifica se termina com 'legal':", frase.endswith("legal"))  # Verifica final
print("   - .isalpha(): Verifica se só contém letras:", frase.isalpha())
print("   - .isalnum(): Verifica se só contém letras e números:", frase.isalnum())  # Letras e números
print("   - .isdigit(): Verifica se só contém dígitos:", frase.isdigit())
print("   - .isspace(): Verifica se só contém espaços:", frase.isspace())  # Só espaços

# Aqui, aplicamos vários métodos de limpeza e substituição na frase fornecida pelo usuário.
print("   - .strip(): Remove espaços do início e fim:", frase.strip())  # Remove espaços extras
print("   - .replace(' ', '_'): Substitui espaços por '_':", frase.replace(" ", "_"))  # Troca espaços por sublinhados

# Aqui, aplicamos vários métodos de contagem e busca na frase fornecida pelo usuário.
print("   - .count('a'): Conta quantas vezes 'a' aparece:", frase.lower().count("a"))  # Conta 'a' (em minúsculas)
print("   - .find('legal'): Índice de 'legal' (ou -1 se não encontrada):", frase.find("legal"))  # Busca 'legal'

# 7. f-strings para formatação de texto
# f-strings permitem inserir variáveis diretamente em uma string usando {}.
# Exemplo: f"Texto {variavel}" insere o valor de variavel no texto.
idade = int(input("Digite sua idade: "))  # Solicita a idade (convertida para inteiro)
print("7. f-strings para formatação:")
print(f"   - Meu nome é {nome_completo} e tenho {idade} anos.")  # Combina nome e idade

# 8. Exercícios práticos
# Tente resolver os exercícios abaixo para praticar os conceitos da aula!
print("   a) Concatene seu nome com a frase ' gosta de programar' e exiba.")
print("   b) Repita a palavra 'Python' 5 vezes com um espaço entre cada repetição.")
print("   c) Acesse o terceiro caractere da sua frase e exiba.")
print("   d) Extraia os últimos 4 caracteres da sua frase (se possível) e exiba.")
print("   e) Use .title() na sua frase e exiba o resultado.")
print("   f) Conte quantas vezes a letra 'e' aparece na sua frase.")
print("   g) Verifique se a palavra 'oi' está na sua frase com .find().")
print("   h) Crie uma f-string dizendo 'Olá, [seu nome], sua frase tem [quantidade] caracteres.'")