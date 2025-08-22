# Exercício 05 - Estruturas de Dados em Python
# Autor: Gabriel Rodrigues

# 1. Crie uma lista com nomes de cinco pessoas. Imprima apenas os nomes que têm mais de 5 letras.
nomes = ["Gabriel", "Ana", "Roberto", "Luiz", "Amanda"]
nomes_maiores = [nome for nome in nomes if len(nome) > 5]
print("Nomes com mais de 5 letras:", nomes_maiores)

# 2. Crie uma tupla com números de 1 a 10. Imprima apenas os números pares usando fatiamento ou compreensão.
numeros_tupla = tuple(range(1, 11))
pares_tupla = tuple(x for x in numeros_tupla if x % 2 == 0)
print("Números pares na tupla:", pares_tupla)

# 3. Crie um dicionário com nomes de alunos e suas notas. Imprima apenas os alunos aprovados (nota >= 7).
alunos = {"Gabriel": 8.5, "Ana": 6.0, "Roberto": 7.2, "Luiz": 4.5, "Amanda": 9.0}
aprovados = {nome: nota for nome, nota in alunos.items() if nota >= 7}
print("Alunos aprovados:", aprovados)

# 4. Crie dois conjuntos: um com números de 1 a 10 e outro com números de 5 a 15. Imprima a interseção e a diferença.
conjunto1 = set(range(1, 11))
conjunto2 = set(range(5, 16))
print("Interseção:", conjunto1 & conjunto2)
print("Diferença (conjunto1 - conjunto2):", conjunto1 - conjunto2)

# 5. Crie um frozenset com as letras da palavra "pythonista". Imprima as letras únicas em ordem alfabética.
letras = frozenset("pythonista")
print("Letras únicas:", sorted(letras))

# 6. Usando list comprehension, crie uma lista com o quadrado dos números ímpares de 1 a 20.
quadrados_impares = [x**2 for x in range(1, 21) if x % 2 != 0]
print("Quadrados dos ímpares:", quadrados_impares)

# 7. Usando dict comprehension, crie um dicionário que mapeia cada letra da palavra "banana" para sua quantidade de ocorrências.
palavra = "banana"
contagem_letras = {letra: palavra.count(letra) for letra in set(palavra)}
print("Contagem de letras:", contagem_letras)

# 8. Crie uma lista de tuplas com nome e idade. Imprima apenas os nomes das pessoas com idade maior que 18.
pessoas = [("Gabriel", 25), ("Ana", 17), ("Roberto", 19), ("Luiz", 15), ("Amanda", 22)]
maiores_idade = [nome for nome, idade in pessoas if idade > 18]
print("Maiores de idade:", maiores_idade)

# 9. Crie um dicionário com produtos e preços. Imprima apenas os produtos com preço acima de R$ 50.
produtos = {"Mouse": 45.0, "Teclado": 75.0, "Monitor": 320.0, "Cabo USB": 15.0, "Webcam": 60.0}
produtos_caros = {produto: preco for produto, preco in produtos.items() if preco > 50}
print("Produtos acima de R$ 50:", produtos_caros)

# 10. Crie um conjunto com nomes de cidades. Peça ao usuário uma cidade e verifique se ela está no conjunto.
cidades = {"São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"}
cidade_usuario = input("Digite o nome de uma cidade: ")
if cidade_usuario in cidades:
    print("Cidade encontrada!")
else:
    print("Cidade não está na lista.")