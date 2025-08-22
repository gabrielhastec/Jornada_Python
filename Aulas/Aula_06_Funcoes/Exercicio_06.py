# Exercício 06 - Funções em Python
# Autor: Gabriel Rodrigues

# 1. Crie uma função que receba uma lista de números e retorne uma nova lista apenas com os números ímpares.
def filtrar_impares(lista):
    return [x for x in lista if x % 2 != 0]

# 2. Crie uma função que receba uma string e retorne quantas vogais ela possui.
def contar_vogais(s):
    return sum(1 for letra in s.lower() if letra in "aeiou")

# 3. Crie uma função que receba um número e retorne sua tabuada de 1 a 10 como uma lista de strings.
def tabuada(n):
    return [f"{n} x {i} = {n*i}" for i in range(1, 11)]

# 4. Crie uma função que receba uma lista de números e retorne o menor valor.
def menor_numero(lista):
    return min(lista) if lista else None

# 5. Crie uma função que receba um dicionário de produtos e preços e retorne a média dos preços.
def media_precos(produtos):
    return sum(produtos.values()) / len(produtos) if produtos else 0

# 6. Crie uma função recursiva que calcule a soma dos números de 1 até n.
def soma_recursiva(n):
    return n if n <= 1 else n + soma_recursiva(n-1)

# 7. Crie uma função decoradora que exibe "Iniciando função..." antes e "Função finalizada." depois da execução.
def log_decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Iniciando função...")
        resultado = funcao(*args, **kwargs)
        print("Função finalizada.")
        return resultado
    return wrapper

@log_decorador
def saudacao_log(nome):
    print(f"Olá, {nome}!")

# 8. Crie uma função que recebe uma lista de nomes e retorna um dicionário com o nome e o número de letras de cada um.
def nomes_com_tamanho(lista):
    return {nome: len(nome) for nome in lista}

# 9. Crie uma função lambda que recebe dois números e retorna o maior.
maior_lambda = lambda a, b: a if a > b else b

# 10. Crie uma função que recebe uma lista de números e retorna uma lista com o quadrado de cada número.
def quadrados(lista):
    return [x**2 for x in lista]

# Testes rápidos
if __name__ == "__main__":
    print("Impares:", filtrar_impares([1,2,3,4,5,6,7]))
    print("Vogais em 'Pythonista':", contar_vogais("Pythonista"))
    print("Tabuada do 7:", tabuada(7))
    print("Menor número:", menor_numero([10, 5, 3, 8]))
    print("Média dos preços:", media_precos({"Mouse": 45, "Teclado": 75, "Monitor": 320}))
    print("Soma recursiva até 5:", soma_recursiva(5))
    saudacao_log("Gabriel")
    print("Nomes e tamanhos:", nomes_com_tamanho(["Ana", "Gabriel", "Luiz"]))
    print("Maior (lambda):", maior_lambda(10, 20))
    print("Quadrados:", quadrados([2, 4, 6]))