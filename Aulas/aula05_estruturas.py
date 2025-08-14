# Aula 05 - Estruturas de Dados em Python
# Nesta aula, vamos explorar as principais estruturas de dados em Python, que nos permitem armazenar e organizar informações de maneira eficiente.  

# 1. Listas
# Listas são coleções ordenadas e mutáveis de itens.
print("1. Listas:")
frutas = ["maçã", "banana", "laranja"]  # Cria uma lista de frutas
print("   - Lista inicial:", frutas)

#Operações com listas -Adicionar:
frutas.append("uva")  # Adiciona "uva" ao final da lista
print("   - Após append('uva'):", frutas)
frutas.extend(["pera", "abacaxi"])  # Adiciona várias frutas ao final da lista
print("   - Após extend(['pera', 'abacaxi']):", frutas)

#Operações com listas -Inserir:
frutas.insert(1, "kiwi")  # Insere "kiwi" na posição 1
print("   - Após insert(1, 'kiwi'):", frutas)

#Operações com listas -Ordenar:
frutas.sort()  # Ordena a lista de frutas
print("   - Após sort():", frutas)

#Operações com listas -Remover:
frutas.remove("banana")  # Remove "banana" da lista
print("   - Após remove('banana'):", frutas)
frutas.pop()  # Remove o último item da lista
print("   - Após pop():", frutas)
frutas.clear()  # Limpa a lista
print("   - Após clear():", frutas)

print("   - Acessando o primeiro item:", frutas[0]) # Acessa o primeiro item
print("   - Comprimento da lista:", len(frutas))  # Tamanho da lista
print() 

# 2. Tuplas
# Tuplas são coleções ordenadas e imutáveis de itens.
print("2. Tuplas:")
coordenadas = (10.0, 20.0)  # Cria uma tupla de coordenadas
print("   - Tupla inicial:", coordenadas)   
print("   - Acessando o primeiro item:", coordenadas[0])  # Acessa o primeiro item
print("   - Comprimento da tupla:", len(coordenadas))  # Tamanho da tupla
print()

# 3. Dicionários
# Dicionários são coleções não ordenadas de pares chave-valor.
print("3. Dicionários:")
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}  # Cria um dicionário
print("   - Dicionário inicial:", pessoa)   
print("   - Acessando o valor da chave 'nome':", pessoa["nome"])  # Acessa o valor associado à chave 'nome'

pessoa["idade"] = 31  # Atualiza o valor da chave 'idade'
print("   - Após atualizar 'idade':", pessoa)   
pessoa["profissão"] = "Engenheira"  # Adiciona uma nova chave-valor
print("   - Após adicionar 'profissão':", pessoa)
pessoa.update({"email": "meu_email@mail.com"})  # Atualiza ou adiciona várias chaves-valor
print("   - Após update com 'email':", pessoa)   
del pessoa["cidade"]  # Remove a chave 'cidade'
print("   - Após deletar 'cidade':", pessoa)   
print("   - Verificando se 'nome' está no dicionário:", "nome" in pessoa)  # Verifica se a chave 'nome' está no dicionário
print("   - Verificando se 'endereço' não está no dicionário:", "endereço" not in pessoa)  # Verifica se a chave 'endereço' não está no dicionário 
                
print("   - Chaves do dicionário:", list(pessoa.keys()))  # Lista de chaves
print("   - Valores do dicionário:", list(pessoa.values()))  # Lista de valores
print() 

# 4. Conjuntos (Sets)
# Conjuntos são coleções não ordenadas de itens únicos.
print("4. Conjuntos (Sets):")
numeros = {1, 2, 3, 4, 5}  # Cria um conjunto de números
print("   - Conjunto inicial:", numeros)
numeros.add(6)  # Adiciona o número 6 ao conjunto
print("   - Após add(6):", numeros)
numeros.remove(3)  # Remove o número 3 do conjunto
print("   - Após remove(3):", numeros)    
print("   - Verificando se 4 está no conjunto:", 4 in numeros)  # Verifica se 4 está no conjunto
print("   - Comprimento do conjunto:", len(numeros))  # Tamanho do conjunto
print() 
numeros.discard(7)  # Tenta remover 7, mas não gera erro se não existir
print("   - Após discard(7):", numeros)
numeros.clear()  # Limpa o conjunto
print("   - Após clear():", numeros)    
print("   - Conjunto após clear():", numeros)  # Mostra o conjunto após limpar
print()

# 4.1. Operações com Conjuntos
# Operações como união, interseção e diferença entre conjuntos.
print("4.1. Operações com Conjuntos:")
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print("   - Conjunto A:", conjunto_a)
print("   - Conjunto B:", conjunto_b)
print("   - União (A | B):", conjunto_a | conjunto_b)  # União dos conjuntos
print("   - Interseção (A & B):", conjunto_a & conjunto_b)  # Interseção dos conjuntos
print("   - Diferença (A - B):", conjunto_a - conjunto_b)  # Diferença do conjunto A em relação ao B
print("   - Diferença simétrica (A ^ B):", conjunto_a ^ conjunto_b)  # Diferença simétrica entre os conjuntos
print("   - Verificando se A é subconjunto de B:", conjunto_a.issubset(conjunto_b))  # Verifica se A é subconjunto de B
print("   - Verificando se A é superconjunto de B:", conjunto_a.issuperset(conjunto_b))  # Verifica se A é superconjunto de B
print("   - Verificando se A e B são disjuntos:", conjunto_a.isdisjoint(conjunto_b))  # Verifica se A e B não têm elementos em comum
print() 

# 4.2. Conjuntos Imutáveis (Frozenset)
# Frozensets são conjuntos imutáveis.
print("4.2. Conjuntos Imutáveis (Frozenset):")
conjunto_imutavel = frozenset([1, 2, 3])  # Cria um frozenset
print("   - Frozenset inicial:", conjunto_imutavel)
print("   - Acessando elementos do frozenset:", list(conjunto_imutavel)[0])  # Acessa o primeiro elemento do frozenset
print("   - Comprimento do frozenset:", len(conjunto_imutavel)) # Tamanho do frozenset
print("   - Verificando se 2 está no frozenset:", 2 in conjunto_imutavel)  # Verifica se 2 está no frozenset
print("   - Verificando se 4 não está no frozenset:", 4 not in conjunto_imutavel)  # Verifica se 4 não está no frozenset
print("   - Frozenset após tentativa de modificação (não é possível):", conjunto_imutavel)  # Mostra o frozenset após tentativa de modificação (não é possível)
print() 

# 4.3. Operações com Conjuntos Imutáveis
# Operações como união, interseção e diferença entre conjuntos imutáveis.
print("4.3. Operações com Conjuntos Imutáveis:")    
conjunto_a = frozenset([1, 2, 3])
conjunto_b = frozenset([3, 4, 5])
print("   - Conjunto A (Frozenset):", conjunto_a)
print("   - Conjunto B (Frozenset):", conjunto_b)
print("   - União (A | B):", conjunto_a | conjunto_b)  # União dos conjuntos imutáveis
print("   - Interseção (A & B):", conjunto_a & conjunto_b)  # Interseção dos conjuntos imutáveis
print("   - Diferença (A - B):", conjunto_a - conjunto_b)  # Diferença do conjunto A em relação ao B
print("   - Diferença simétrica (A ^ B):", conjunto_a ^ conjunto_b)  # Diferença simétrica entre os conjuntos imutáveis
print("   - Verificando se A é subconjunto de B:", conjunto_a.issubset(conjunto_b))  # Verifica se A é subconjunto de B
print("   - Verificando se A é superconjunto de B:", conjunto_a.issuperset(conjunto_b))  # Verifica se A é superconjunto de B
print("   - Verificando se A e B são disjuntos:", conjunto_a.isdisjoint(conjunto_b))  # Verifica se A e B não têm elementos em comum
print("   - Frozenset A após operações:", conjunto_a)   # Mostra o frozenset A após operações
print("   - Frozenset B após operações:", conjunto_b)   # Mostra o frozenset B após operações
print()

# 4.4. Iterando sobre Estruturas de Dados
# Podemos iterar sobre listas, tuplas, dicionários e conjuntos.
print("4.4. Iterando sobre Estruturas de Dados:")
print("   - Iterando sobre lista de frutas:")
for fruta in frutas:
    print("      -", fruta)
print("   - Iterando sobre tupla de coordenadas:")
for coord in coordenadas:
    print("      -", coord)
print("   - Iterando sobre dicionário de pessoa:")
for chave, valor in pessoa.items():
    print("      -", chave + ":", valor)
print("   - Iterando sobre conjunto de números:")
for numero in numeros:
    print("      -", numero)    
print("   - Iterando sobre frozenset de conjunto imutável:")
for numero in conjunto_imutavel:
    print("      -", numero)    
print("   - Iteração concluída")
print() 

# 5. List Comprehensions
# List comprehensions são uma maneira concisa de criar listas.
print("5. List Comprehensions:")
quadrados = [x**2 for x in range(10)]  # Cria uma lista de quadrados de 0 a 9
print("   - Lista de quadrados:", quadrados)    
pares = [x for x in range(20) if x % 2 == 0]  # Cria uma lista de números pares de 0 a 19
print("   - Lista de números pares:", pares)    
dicionario_frutas = {fruta: len(fruta) for fruta in frutas}  # Cria um dicionário com frutas e seus comprimentos
print("   - Dicionário de frutas e seus comprimentos:", dicionario_frutas)    
tupla_numeros = tuple(x for x in range(5))  # Cria uma tupla de números de 0 a 4
print("   - Tupla de números:", tupla_numeros)    
conjunto_numeros = {x for x in range(5)}  # Cria um conjunto de números de 0 a 4
print("   - Conjunto de números:", conjunto_numeros)    
print("   - List comprehensions concluídas")
print() 

# 6. Dicionário Comprehensions
# Dicionário comprehensions são uma maneira concisa de criar dicionários.
print("6. Dicionário Comprehensions:")
dicionario_quadrados = {x: x**2 for x in range(10)}  # Cria um dicionário com números e seus quadrados
print("   - Dicionário de quadrados:", dicionario_quadrados)    
dicionario_pares = {x: "par" for x in range(20) if x % 2 == 0}  # Cria um dicionário com números pares e a string "par"
print("   - Dicionário de números pares:", dicionario_pares)    
dicionario_frutas = {fruta: len(fruta) for fruta in ["maçã", "banana", "laranja"]}  # Cria um dicionário com frutas e seus comprimentos
print("   - Dicionário de frutas e seus comprimentos:", dicionario_frutas)    
print("   - Dicionário comprehensions concluídas")
print() 

## Exercício Prático
# Peça ao usuário para inserir nomes de frutas até que ele digite "sair". Armazene esses nomes em uma lista e, ao final, mostre a lista completa de frutas inseridas.
frutas_usuario = []  # Lista para armazenar frutas inseridas pelo usuário   
while True:
    fruta = input("Digite o nome de uma fruta (ou 'sair' para terminar): ")
    if fruta.lower() == "sair": # Verifica se o usuário quer sair   
        break
    frutas_usuario.append(fruta)  # Adiciona a fruta à lista
print("   - Frutas inseridas:", frutas_usuario)   
print("   - Fim do exercício prático")
print() 

# Crie um programa que utilize um dicionário para armazenar informações de um livro (título, autor, ano) e permita ao usuário atualizar o ano de publicação.
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}   
print("Informações do livro:", livro)   
novo_ano = int(input("Digite o novo ano de publicação: "))   
livro["ano"] = novo_ano  # Atualiza o ano de publicação
print("   - Informações atualizadas do livro:", livro)   
print("   - Fim do exercício de revisão")
print() 

# Crie um programa que peça ao usuário para inserir dois números e mostre se o primeiro é maior, menor ou igual ao segundo.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("   - O primeiro número é maior que o segundo.")  
elif num1 < num2:
    print("   - O primeiro número é menor que o segundo.")  
else:
    print("   - Os números são iguais.")    
print("   - Fim do exercício de revisão")
print() 
