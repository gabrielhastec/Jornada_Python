# Aula 05 - Estruturas de Dados em Python
# Nesta aula, vamos explorar as principais estruturas de dados em Python, que nos permitem armazenar e organizar informações de maneira eficiente.  

# 1. Listas
# Listas são coleções ordenadas e mutáveis de itens.
# Elas podem conter elementos de diferentes tipos e são definidas usando colchetes [].
# As listas são úteis para armazenar sequências de dados que podem ser alteradas ao longo do tempo.
print("1. Listas:")
frutas = ["maçã", "banana", "laranja"]  # Cria uma lista de frutas
print("   - Lista inicial:", frutas)

# Operações com listas -Adicionar:
# Podemos adicionar itens ao final da lista usando append() ou extend().
# O método append() adiciona um único item ao final da lista.
# O método extend() adiciona vários itens ao final da lista.
# O método copy() cria uma cópia da lista.
print("   - Adicionando itens:")
frutas.append("uva")  # Adiciona "uva" ao final da lista
print("   - Após append('uva'):", frutas)
frutas.extend(["pera", "abacaxi"])  # Adiciona várias frutas ao final da lista
print("   - Após extend(['pera', 'abacaxi']):", frutas)
frutas = frutas.copy()  # Cria uma cópia da lista de frutas
print("   - Após copy():", frutas)

# Operações com listas -Concatenar:
# Podemos concatenar duas listas usando o operador +.
# O operador + cria uma nova lista que é a junção de duas listas.
print("   - Concatenando listas:")
outras_frutas = ["kiwi", "manga"]
frutas = frutas + outras_frutas  # Concatena outras_frutas à lista de frutas
print("   - Após concatenação:", frutas)

# Operações com listas -Repetir:
# Podemos repetir uma lista usando o operador *.
# O operador * cria uma nova lista que é a repetição da lista original.
print("   - Repetindo a lista:")
frutas_repetidas = frutas * 2  # Repete a lista de frutas duas vezes
print("   - Após repetição:", frutas_repetidas)

# Operações com listas -Verificar:
# Podemos verificar se um item está na lista usando o operador in.
# O operador in retorna True se o item estiver na lista, caso contrário, retorna False.
print("   - Verificando itens:")
print("   - 'maçã' está na lista?", "maçã" in frutas)  # Verifica se "maçã" está na lista
print("   - 'uva' está na lista?", "uva" in frutas)  # Verifica se "uva" está na lista
print("   - 'abacate' não está na lista?", "abacate" not in frutas)  # Verifica se "abacate" não está na lista

# Operações com listas -Acessar:
# Podemos acessar elementos da lista usando índices.
# A indexação começa em 0, então frutas[0] é "maçã".
print("   - Acessando o segundo item:", frutas[1]) # Acessa o segundo item da lista
print("   - Acessando os últimos dois itens:", frutas[-2:])  # Acessa os últimos dois itens da lista
frutas.index("maçã")  # Retorna o índice da primeira ocorrência de "maçã"
print("   - Índice de 'maçã':", frutas.index("maçã"))

# Operações com listas -Contar:
# O método count() conta quantas vezes um item aparece na lista.
print("   - Contagem de 'banana':", frutas.count("banana"))  # Conta quantas vezes "banana" aparece na lista

# Operações com listas -Inserir:
# O método insert() insere um item em uma posição específica.
frutas.insert(1, "kiwi")  # Insere "kiwi" na posição 1
print("   - Após insert(1, 'kiwi'):", frutas)

# Operações com listas -Ordenar:
# As listas podem ser ordenadas em ordem alfabética ou numérica.
# As listas são ordenadas in-place, ou seja, a lista original é modificada.
print("   - Lista original:", frutas)
frutas.sort()  # Ordena a lista de frutas
print("   - Após sort():", frutas)

# Operações com listas -Reverter:
# O método reverse() inverte a ordem dos itens na lista.
# As listas são revertidas in-place, ou seja, a lista original é modificada.
frutas = ["maçã", "banana", "laranja"]
frutas.reverse()  # Inverte a lista de frutas
print("   - Após reverse():", frutas)

# Operações com listas -Fatiamento:
# Podemos usar fatiamento para obter sublistas.
# O fatiamento é feito usando a sintaxe lista[inicio:fim], onde 'inicio' é inclusivo e 'fim' é exclusivo.
print("   - Fatiamento da lista (do segundo ao quarto item):", frutas[1:4])  # Obtém os itens do índice 1 ao 3

# Operações com listas -Remover:
# O método remove() remove a primeira ocorrência de um item da lista.
# O método pop() remove e retorna o último item da lista.
# O método clear() remove todos os itens da lista.
frutas.remove("banana")  # Remove "banana" da lista
print("   - Após remove('banana'):", frutas)
frutas.pop()  # Remove o último item da lista
print("   - Após pop():", frutas)
frutas.clear()  # Limpa a lista
print("   - Após clear():", frutas)

# Operações com listas -Tamanho:
# O método len() retorna o número de itens na lista.
frutas = ["maçã", "banana", "laranja"]  # Recria a lista de frutas
print("   - Comprimento da lista:", len(frutas))  # Tamanho da lista
print() 

# 2. Tuplas
# Tuplas são coleções ordenadas e imutáveis de itens.
# Tuplas são semelhantes às listas, mas não podem ser modificadas após a criação.
# Elas são úteis para armazenar dados que não devem ser alterados.
# Tuplas são definidas usando parênteses ().
print("2. Tuplas:")
coordenadas = (10.0, 20.0, 30.0)  # Cria uma tupla de coordenadas
print("   - Tupla inicial:", coordenadas)

# Operações com tuplas -Acessar:
# Podemos acessar elementos da tupla usando índices.
print("   - Acessando o segundo item:", coordenadas[1])  # Acessa o segundo item
print("   - Acessando os últimos dois itens:", coordenadas[-2:])  # Acessa os últimos dois itens da tupla

# Operações com tuplas -Contar:
# O método count() conta quantas vezes um item aparece na tupla.
print("   - Contagem de 10.0:", coordenadas.count(10.0))  # Conta quantas vezes 10.0 aparece na tupla

# Operações com tuplas -Indexar:
# O método index() retorna o índice da primeira ocorrência de um item na tupla.
print("   - Índice de 20.0:", coordenadas.index(20.0))  # Retorna o índice da primeira ocorrência de 20.0

# Operações com tuplas -Fatiamento:
# Podemos usar fatiamento para obter subtuplas.
print("   - Fatiamento da tupla (do primeiro ao segundo item):", coordenadas[0:2])  # Obtém os itens do índice 0 ao 1

# Operações com tuplas -Tamanho:
print("   - Comprimento da tupla:", len(coordenadas))  # Tamanho da tupla

# Operações com tuplas -Imutabilidade:
# Tuplas são imutáveis, ou seja, não podem ser modificadas após a criação.
# Isso significa que não podemos adicionar, remover ou alterar itens em uma tupla.
# No entanto, podemos criar uma nova tupla a partir de uma tupla existente.
# Operações com tuplas -Criar nova tupla:
nova_tupla = coordenadas + (30.0,)  # Cria uma nova tupla adicionando 30.0
print("   - Nova tupla após adição de 30.0:", nova_tupla)  # Mostra a nova tupla

# Operações com tuplas -Converter para lista:
# Podemos converter uma tupla em uma lista usando a função list().
nova_lista = list(nova_tupla)  # Converte a nova tupla em uma lista
print("   - Nova lista a partir da nova tupla:", nova_lista)  # Mostra a nova lista

# Operações com tuplas -Converter para conjunto:
# Podemos converter uma tupla em um conjunto usando a função set().
# Conjuntos são coleções não ordenadas de itens únicos.
print("   - Convertendo nova tupla para conjunto:")
# Tuplas podem ser usadas para criar conjuntos, mas os conjuntos não mantêm a ordem dos itens.
nova_tupla = (1, 2, 3, 4, 5)  # Exemplo de nova tupla
# Converte a nova tupla em um conjunto
nova_conjunto = set(nova_tupla)  # Converte a nova tupla em um conjunto
print("   - Novo conjunto a partir da nova tupla:", nova_conjunto)  # Mostra o novo conjunto

# Operações com tuplas -Converter para dicionário:
# Tuplas podem ser usadas para criar dicionários, mas precisamos de pares chave-valor.
# Por exemplo, podemos usar uma tupla de tuplas para criar um dicionário.
print("   - Convertendo tupla de tuplas para dicionário:")
tupla_dicionario = (("nome", "Alice"), ("idade", 30), ("cidade", "São Paulo"))
novo_dicionario = dict(tupla_dicionario)  # Converte a tupla de tuplas em um dicionário
print("   - Novo dicionário a partir da tupla de tuplas:", novo_dicionario)  # Mostra o novo dicionário

# Operações com tuplas -Converter para string:
# Podemos converter uma tupla em uma string usando a função join().
# No entanto, precisamos garantir que todos os itens sejam strings.
print("   - Convertendo tupla para string:")
tupla_string = ("Python", "é", "legal")
tupla_string = " ".join(tupla_string)  # Converte a tupla em uma string
print("   - Tupla convertida para string:", tupla_string)  # Mostra a tupla convertida para string

# 3. Dicionários
# Dicionários são coleções não ordenadas de pares chave-valor.
# Eles são úteis para armazenar dados que precisam ser acessados por uma chave.
# Dicionários são definidos usando chaves {}.
# Cada chave deve ser única e é usada para acessar o valor associado.
print("3. Dicionários:")
# Cria um dicionário com informações de uma pessoa
print("   - Dicionário inicial:")
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}  # Cria um dicionário
print("   - Dicionário inicial:", pessoa)

# Operações com dicionários -Acessar:
# Podemos acessar valores usando suas chaves.
print("   - Acessando o valor da chave 'nome':", pessoa["nome"])  # Acessa o valor associado à chave 'nome'
print("   - Acessando o valor da chave 'idade':", pessoa["idade"])  # Acessa o valor associado à chave 'idade')

# Operações com dicionários -Adicionar:
# Podemos adicionar novos pares chave-valor ao dicionário.
pessoa["profissão"] = "Engenheira"  # Adiciona uma nova chave-valor
print("   - Após adicionar 'profissão':", pessoa)  # Mostra o dicionário após adicionar a nova chave-valor

# Operações com dicionários -Atualizar:
# Podemos atualizar o valor de uma chave existente.
pessoa["idade"] = 31  # Atualiza o valor da chave 'idade'
print("   - Após atualizar 'idade':", pessoa)  # Mostra o dicionário após atualizar o valor da chave 'idade'

# Operações com dicionários -Remover:
# Podemos remover um par chave-valor usando o método pop() ou del.
# O método pop() remove e retorna o valor associado à chave.
pessoa.pop("cidade")  # Remove a chave 'cidade' e retorna seu valor
print("   - Após pop('cidade'):", pessoa)  # Mostra o dicionário após remover a chave 'cidade'
# O comando del é usado para remover uma chave e seu valor associado do dicionário.

# 4. Conjuntos (Sets)
# Conjuntos são coleções não ordenadas de itens únicos.
# Eles são úteis para armazenar dados que não precisam manter a ordem e não podem ter duplicatas.
# Conjuntos são definidos usando chaves {} ou a função set().
print("4. Conjuntos (Sets):")
numeros = {1, 2, 3, 4, 5}  # Cria um conjunto de números
print("   - Conjunto inicial:", numeros)

# 4.1. Operações com Conjuntos
# Operações com conjuntos -Adicionar:
# Podemos adicionar itens ao conjunto usando o método add().
# O método add() adiciona um único item ao conjunto.
numeros.add(7)  # Adiciona o número 7 ao conjunto
print("   - Após add(7):", numeros)

# Operações com conjuntos -Remover:
# Podemos remover itens do conjunto usando o método remove() ou discard().
# O método remove() remove um item específico e gera um erro se o item não existir.
numeros.remove(3)  # Remove o número 3 do conjunto
print("   - Após remove(3):", numeros)
# O método discard() remove um item específico, mas não gera erro se o item não existir.
numeros.discard(10)  # Tenta remover o número 10, mas não gera erro
print("   - Após discard(10):", numeros)

# Operações com conjuntos -Verificar:
# Podemos verificar se um item está no conjunto usando o operador in.
print("   - Verificando se 2 está no conjunto:", 2 in numeros)  # Verifica se 2 está no conjunto
print("   - Verificando se 10 não está no conjunto:", 10 not in numeros)  # Verifica se 10 não está no conjunto

# Operações como união, interseção e diferença entre conjuntos.
print("   - Operações com conjuntos:")
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print("   - Conjunto A:", conjunto_a)
print("   - Conjunto B:", conjunto_b)
# União dos conjuntos:
# A união de dois conjuntos é um novo conjunto que contém todos os elementos de ambos os conjuntos.
## A união é feita usando o operador | ou o método union().
print("   - União (A | B):", conjunto_a | conjunto_b)  # União dos conjuntos
# Interseção dos conjuntos:
# A interseção de dois conjuntos é um novo conjunto que contém apenas os elementos que estão em ambos os conjuntos.
## A interseção é feita usando o operador & ou o método intersection().
print("   - Interseção (A & B):", conjunto_a & conjunto_b)  # Interseção dos conjuntos
# Diferença do conjunto A em relação ao B:
# A diferença de dois conjuntos é um novo conjunto que contém os elementos que estão no primeiro conjunto, mas não no segundo.
## A diferença é feita usando o operador - ou o método difference().
print("   - Diferença (A - B):", conjunto_a - conjunto_b)  # Diferença do conjunto A em relação ao B
# Diferença simétrica entre os conjuntos:
# A diferença simétrica de dois conjuntos é um novo conjunto que contém os elementos que estão em um dos conjuntos, mas não em ambos.
## A diferença simétrica é feita usando o operador ^ ou o método symmetric_difference().
print("   - Diferença simétrica (A ^ B):", conjunto_a ^ conjunto_b)  # Diferença simétrica entre os conjuntos
# Verificando se A é subconjunto de B:
# Um conjunto A é um subconjunto de B se todos os elementos de A estão em B.
## A verificação é feita usando o método issubset().
print("   - Verificando se A é subconjunto de B:", conjunto_a.issubset(conjunto_b))  # Verifica se A é subconjunto de B

# 4.2. Conjuntos Imutáveis (Frozenset)
# Frozensets são conjuntos imutáveis.
# Eles são úteis quando precisamos de um conjunto que não pode ser modificado após a criação.
# Frozensets são definidos usando a função frozenset().
print("4.2. Conjuntos Imutáveis (Frozenset):")
# Cria um frozenset com números
numeros_imutaveis = frozenset([1, 2, 3])  # Cria um frozenset de números
print("   - Frozenset inicial:", numeros_imutaveis)
# Acessando elementos do frozenset:
# Podemos acessar elementos do frozenset convertendo-o para uma lista ou usando um loop.
print("   - Acessando elementos do frozenset:", list(numeros_imutaveis)[0])  # Acessa o primeiro elemento do frozenset
# Comprimento do frozenset:
# Podemos obter o tamanho do frozenset usando a função len().
print("   - Comprimento do frozenset:", len(numeros_imutaveis))  # Tamanho do frozenset
# Verificando se um item está no frozenset:
# Podemos verificar se um item está no frozenset usando o operador in.
print("   - Verificando se 2 está no frozenset:", 2 in numeros_imutaveis)  # Verifica se 2 está no frozenset
# Verificando se um item não está no frozenset:
# Podemos verificar se um item não está no frozenset usando o operador not in.
print("   - Verificando se 4 não está no frozenset:", 4 not in numeros_imutaveis)  # Verifica se 4 não está no frozenset

# 4.3. Operações com Conjuntos Imutáveis
# Operações como união, interseção e diferença entre conjuntos imutáveis.
# Frozensets suportam as mesmas operações que conjuntos mutáveis, mas não podem ser modificados.
print("4.3. Operações com Conjuntos Imutáveis:")    
# Cria dois frozensets para demonstrar as operações
# Frozensets são úteis quando precisamos de conjuntos que não podem ser alterados.
# Eles são imutáveis, o que significa que não podemos adicionar ou remover itens após a criação.
conjunto_a = frozenset([1, 2, 3])
conjunto_b = frozenset([3, 4, 5])
# Exibe os conjuntos imutáveis e as operações entre eles
print("   - Conjuntos Imutáveis:")
print("   - Conjunto A (Frozenset):", conjunto_a)
print("   - Conjunto B (Frozenset):", conjunto_b)
# Operações com conjuntos imutáveis -União, interseção, diferença e diferença simétrica
# Podemos realizar operações como união, interseção, diferença e diferença simétrica entre conjuntos imutáveis.
print("   - Operações com conjuntos imutáveis:")
# União dos conjuntos imutáveis:
# A união de dois conjuntos imutáveis é um novo conjunto que contém todos os elementos de ambos os conjuntos.
print("   - União (A | B):", conjunto_a | conjunto_b)  # União dos conjuntos imutáveis
# Interseção dos conjuntos imutáveis:
# A interseção de dois conjuntos imutáveis é um novo conjunto que contém apenas os elementos que estão em ambos os conjuntos.
print("   - Interseção (A & B):", conjunto_a & conjunto_b)  # Interseção dos conjuntos imutáveis
# Diferença do conjunto A em relação ao B:
# A diferença de dois conjuntos imutáveis é um novo conjunto que contém os elementos que estão no primeiro conjunto, mas não no segundo.
print("   - Diferença (A - B):", conjunto_a - conjunto_b)  # Diferença do conjunto A em relação ao B
# Diferença simétrica entre os conjuntos imutáveis:
# A diferença simétrica de dois conjuntos imutáveis é um novo conjunto que contém os elementos que estão em um dos conjuntos, mas não em ambos.
print("   - Diferença simétrica (A ^ B):", conjunto_a ^ conjunto_b)  # Diferença simétrica entre os conjuntos imutáveis

# 4.4. Iterando sobre Estruturas de Dados
# Podemos iterar sobre as estruturas de dados usando loops.
# A iteração é uma maneira de percorrer os elementos de uma estrutura de dados, como listas, tuplas, dicionários e conjuntos.
print("4.4. Iterando sobre Estruturas de Dados:")
# Iterando sobre uma lista:
# Podemos usar um loop for para iterar sobre os elementos de uma lista.
lista = ["maçã", "banana", "laranja"]
print("   - Iterando sobre a lista:")
for fruta in lista:  # Itera sobre cada fruta na lista
    print("   - Fruta:", fruta)
# Iterando sobre uma tupla:
# Podemos usar um loop for para iterar sobre os elementos de uma tupla.
tupla = ("maçã", "banana", "laranja")
print("   - Iterando sobre a tupla:")
for fruta in tupla:  # Itera sobre cada fruta na tupla
    print("   - Fruta:", fruta)
# Iterando sobre um dicionário:
# Podemos usar um loop for para iterar sobre as chaves ou valores de um dicionário.
dicionario = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
print("   - Iterando sobre o dicionário:")
for chave, valor in dicionario.items():  # Itera sobre cada par chave-valor no dicionário
    print("   - Chave:", chave, "Valor:", valor)
# Iterando sobre um conjunto:
# Podemos usar um loop for para iterar sobre os elementos de um conjunto.
conjunto = {1, 2, 3, 4, 5}
print("   - Iterando sobre o conjunto:")
for numero in conjunto:  # Itera sobre cada número no conjunto
    print("   - Número:", numero)
# Iterando sobre um frozenset:
# Podemos usar um loop for para iterar sobre os elementos de um frozenset.
frozenset_exemplo = frozenset([1, 2, 3, 4, 5])
print("   - Iterando sobre o frozenset:")
for numero in frozenset_exemplo:  # Itera sobre cada número no frozenset
    print("   - Número:", numero)
print("   - Iteração concluída")
print()

# 5. List Comprehensions
# List comprehensions são uma maneira concisa de criar listas.
# Elas permitem criar listas a partir de outras listas ou iteráveis de forma mais legível e eficiente.
## List comprehensions são definidas usando colchetes [] e podem incluir condições.
print("5. List Comprehensions:")
# Exemplo de list comprehension para criar uma lista de quadrados de números de 0 a 9
quadrados = [x**2 for x in range(10)]  # Cria uma lista com os quadrados dos números de 0 a 9
print("   - Lista de quadrados:", quadrados)  # Mostra a lista de quadrados
# Exemplo de list comprehension com condição para criar uma lista de números pares de 0 a 19
pares = [x for x in range(20) if x % 2 == 0]  # Cria uma lista com os números pares de 0 a 19
print("   - Lista de números pares:", pares)  # Mostra a lista de números pares
# Exemplo de list comprehension para criar uma lista de frutas com seus comprimentos
frutas = ["maçã", "banana", "laranja"]  # Lista de frutas
comprimentos_frutas = [len(fruta) for fruta in frutas]  # Cria uma lista com os comprimentos das frutas
print("   - Lista de comprimentos das frutas:", comprimentos_frutas)  # Mostra a lista de comprimentos das frutas
# Exemplo de list comprehension com condição para criar uma lista de números ímpares de 0 a 19
impares = [x for x in range(20) if x % 2 != 0]  # Cria uma lista com os números ímpares de 0 a 19
print("   - Lista de números ímpares:", impares)  # Mostra a lista de números ímpares
print("   - List comprehensions concluídas")
print()

# 6. Dicionário Comprehensions
# Dicionário comprehensions são uma maneira concisa de criar dicionários.
# Eles permitem criar dicionários a partir de outras listas ou iteráveis de forma mais legível e eficiente.
# Dicionário comprehensions são definidos usando chaves {} e podem incluir condições.
print("6. Dicionário Comprehensions:")
# Exemplo de dicionário comprehension para criar um dicionário com números e seus quadrados
quadrados_dict = {x: x**2 for x in range(10)}  # Cria um dicionário com os números de 0 a 9 e seus quadrados
print("   - Dicionário de quadrados:", quadrados_dict)  # Mostra o dicionário de quadrados
# Exemplo de dicionário comprehension com condição para criar um dicionário com números pares e seus quadrados
pares_dict = {x: x**2 for x in range(20) if x % 2 == 0}  # Cria um dicionário com os números pares de 0 a 19 e seus quadrados
print("   - Dicionário de números pares e seus quadrados:", pares_dict)  # Mostra o dicionário de números pares e seus quadrados
# Exemplo de dicionário comprehension para criar um dicionário com frutas e seus comprimentos
frutas_dict = {fruta: len(fruta) for fruta in ["maçã", "banana", "laranja"]}  # Cria um dicionário com as frutas e seus comprimentos
print("   - Dicionário de comprimentos das frutas:", frutas_dict)  # Mostra o dicionário de comprimentos das frutas
# Exemplo de dicionário comprehension com condição para criar um dicionário com números ímpares e seus quadrados
impares_dict = {x: x**2 for x in range(20) if x % 2 != 0}  # Cria um dicionário com os números ímpares de 0 a 19 e seus quadrados
print("   - Dicionário de números ímpares e seus quadrados:", impares_dict)  # Mostra o dicionário de números ímpares e seus quadrados
print("   - Dicionário comprehensions concluídos")
print()

## Exercício Prático

# 1- Crie uma lista de números de 1 a 10 e use list comprehension para criar uma nova lista com os quadrados desses números.
numeros = list(range(1, 11))
quadrados = [x**2 for x in numeros]  # Cria uma lista com os quadrados dos números de 1 a 10
print("   - Lista de números:", numeros)
print("   - Lista de quadrados:", quadrados)  # Mostra a lista de quadrados

# 2- Crie um dicionário que mapeia cada número de 1 a 10 ao seu cubo usando dicionário comprehension.
cubos_dict = {x: x**3 for x in range(1, 11)}  # Cria um dicionário com os números de 1 a 10 e seus cubos
print("   - Dicionário de cubos:", cubos_dict)  # Mostra o dicionário de cubos

# 3- Crie um conjunto com os números pares de 1 a 20 e use operações de conjuntos para encontrar a união com outro conjunto de números ímpares.
numeros_pares = {x for x in range(1, 21) if x % 2 == 0}  # Cria um conjunto com os números pares de 1 a 20
numeros_impares = {x for x in range(1, 21) if x % 2 != 0}  # Cria um conjunto com os números ímpares de 1 a 20
uniao_conjuntos = numeros_pares | numeros_impares  # União dos conjuntos de números pares e ímpares
print("   - Conjunto de números pares:", numeros_pares) 
print("   - Conjunto de números ímpares:", numeros_impares)  # Mostra o conjunto de números ímpares
print("   - União dos conjuntos:", uniao_conjuntos)  # Mostra a união dos conjuntos de números pares e ímpares

# 4- Crie uma tupla com os nomes de três frutas e use fatiamento para acessar o segundo nome.
frutas_tupla = ("maçã", "banana", "laranja")
print("   - Tupla de frutas:", frutas_tupla)  # Mostra a tupla de frutas
segundo_fruta = frutas_tupla[1]  # Acessa o segundo nome da tupla
print("   - Segundo nome da tupla:", segundo_fruta)  # Mostra o segundo nome da tupla

# 5- Crie um dicionário com informações de uma pessoa (nome, idade, cidade) e use o método keys() para obter as chaves do dicionário.
pessoa_info = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
print("   - Dicionário de informações da pessoa:", pessoa_info)  # Mostra o dicionário de informações da pessoa
chaves_dicionario = pessoa_info.keys()  # Obtém as chaves do dicionário
print("   - Chaves do dicionário:", chaves_dicionario)  # Mostra as chaves do dicionário
