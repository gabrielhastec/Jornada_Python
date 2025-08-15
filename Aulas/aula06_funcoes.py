# Aula 06 - Funções em Python
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
# Elas podem receber parâmetros, retornar valores e até mesmo ser aninhadas ou decoradas.
# Neste arquivo, veremos exemplos de funções simples, matemáticas, manipulação de listas, recursivas, decoradoras e mais.

# Importante: Sempre documente suas funções com docstrings para facilitar o entendimento.

# Função simples
# Esta função exibe uma saudação personalizada.
def saudacao(nome="Visitante"): # Exemplo de função com parâmetro padrão
    """
    Exibe uma saudação personalizada.
    """
    print(f"Olá, {nome}! Bem-vindo(a) à aula de funções.")

# Funções matemáticas básicas
# Estas funções realizam operações matemáticas simples.
def soma(a, b): return a + b    
def subtracao(a, b): return a - b   
def multiplicacao(a, b): return a * b   
def divisao(a, b):  
    if b == 0:  
        raise ValueError("Divisão por zero não é permitida.")   
    return a / b    

# Funções para manipulação de listas
# Estas funções realizam operações comuns em listas.
def media(lista): return sum(lista) / len(lista) if lista else 0    
def maximo(lista): return max(lista) if lista else None 
def minimo(lista): return min(lista) if lista else None

# Funções com parâmetros opcionais
# Esta função conta de um número inicial a um número final, com um passo opcional.
def contador(inicio, fim, passo=1):
    if passo <= 0:
        raise ValueError("O passo deve ser positivo.")
    for i in range(inicio, fim + 1, passo):
        print(i, end=' ')
    print()

# Função que verifica se um número é par ou ímpar
# Esta função retorna "Par" ou "Ímpar" com base no número fornecido.
# O % operador é usado para verificar a paridade.
def par_ou_impar(numero): return "Par" if numero % 2 == 0 else "Ímpar"

# Funções para cálculo de áreas
# Estas funções calculam a área de diferentes formas geométricas.
def area_retangulo(base, altura): return base * altura
def area_circulo(raio):
    import math
    return math.pi * (raio ** 2)
def area_triangulo(base, altura): return (base * altura) / 2
def area_quadrado(lado): return lado ** 2

# 2. Funções lambda
# Funções anônimas para operações simples.
# Estas funções são úteis para operações rápidas e pequenas.
# Exemplo de função lambda para soma e verificação de paridade.
# Funções lambda são úteis para operações simples e podem ser usadas como argumentos em outras funções.
soma_lambda = lambda x, y: x + y
par_lambda = lambda x: x % 2 == 0

# Funções recursivas
# Estas funções chamam a si mesmas para resolver problemas.
# Exemplo de função recursiva para calcular fatorial e Fibonacci.
def fatorial(n): return 1 if n <= 1 else n * fatorial(n - 1)
def fibonacci(n): return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# Funções decoradoras
# Estas funções modificam o comportamento de outras funções.
def decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Antes de chamar a função.")
        resultado = funcao(*args, **kwargs)
        print("Depois de chamar a função.")
        return resultado
    return wrapper

@decorador
def saudacao_decorada(nome):
    print(f"Olá, {nome}! Esta é uma função decorada.")

import time
def tempo_execucao(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@tempo_execucao
def exemplo_tempo_execucao(n):
    return sum(range(n))

# Funções aninhadas e de ordem superior
# Estas funções retornam outras funções ou aceitam funções como argumentos.

# Exemplo de função aninhada
# Esta função retorna outra função que multiplica um número por um fator dado.
def funcao_externa(x):
    def funcao_interna(y):
        return x * y
    return funcao_interna

# Exemplo de função de ordem superior
# Esta função aplica uma função a cada elemento de uma lista.
def aplicar_funcao(funcao, lista):
    return [funcao(x) for x in lista]

# Exercícios práticos

# 1. Crie uma função que receba uma lista de números e retorne a soma dos números pares.
def soma_pares(lista):
    return sum(x for x in lista if x % 2 == 0)

# 2. Crie uma função que receba uma string e retorne a string invertida.
def inverter_string(s):
    return s[::-1]

# 3. Crie uma função que receba um número e retorne True se o número for primo e False caso contrário.
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(a, b):
    return a if a > b else b

# 5. Crie uma função que receba uma lista de strings e retorne a lista ordenada em ordem alfabética.
def ordenar_strings(lista):
    return sorted(lista)


# Testando as funções
# Este bloco de código é executado quando o arquivo é executado
# diretamente, permitindo testar as funções definidas acima.
# Você pode comentar ou descomentar as linhas abaixo para testar as funções individualmente.
if __name__ == "__main__":

    # Teste da função de saudação
    saudacao() # Teste da função de saudação com valor padrão
    saudacao_decorada("Maria")

    # Teste das funções matemáticas
    print("Soma: ", soma(5, 3))
    print("Subtração: ", subtracao(5, 3))
    print("Multiplicação: ", multiplicacao(5, 3))
    print("Divisão: ", divisao(5, 0.5))

    # Teste das funções de manipulação de listas
    print("Média: ", media([1, 2, 3, 4, 5]))
    print("Máximo: ", maximo([1, 2, 3, 4, 5]))
    print("Mínimo: ", minimo([1, 2, 3, 4, 5]))

    # Teste da função contador
    contador(1, 10, 2)
    contador(5, 15)  # Usando o passo padrão

    # Teste da função par_ou_impar
    print("Número 4 é: ", par_ou_impar(4))
    print("Número 7 é: ", par_ou_impar(7))

    # Teste das funções de cálculo de áreas
    print("Área do retângulo (5x10): ", area_retangulo(5, 10))
    print("Área do círculo (raio 7): ", area_circulo(7))
    print("Área do triângulo (base 5, altura 10): ", area_triangulo(5, 10))
    print("Área do quadrado (lado 4): ", area_quadrado(4))

    # Teste das funções lambda
    print("Soma usando lambda: ", soma_lambda(10, 20))
    print("Número 8 é par? ", par_lambda(8))
    print("Número 9 é par? ", par_lambda(9))

    # Teste das funções recursivas
    print("Fatorial de 5: ", fatorial(5))
    print("Fibonacci de 6: ", fibonacci(6))

    # Teste da função de tempo de execução
    exemplo_tempo_execucao(1000000)

    # Teste das funções aninhadas e de ordem superior
    funcao = funcao_externa(5)
    print("Função aninhada (5 * 3): ", funcao(3))
    print("Função de ordem superior (aplicar função lambda): ", aplicar_funcao(par_lambda, [1, 2, 3, 4, 5]))
