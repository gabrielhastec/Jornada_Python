
# 🚀 Jornada Python – Meu Aprendizado Passo a Passo

Este repositório documenta minha evolução no aprendizado de **Python**, desde conceitos iniciais até a criação de projetos.
O objetivo é mostrar **não apenas o resultado**, mas **o processo de aprendizado**, com códigos de aulas, exemplos práticos e exercícios.

---

## 🗂 Estrutura do Repositório

* **📂 aulas/** → códigos e anotações de cada aula.
* **📂 projetos/** → projetos que aplicam os conhecimentos adquiridos.
* **📄 README.md** → índice das aulas, conceitos aprendidos e exemplos.

> Este registro funciona como um **portfólio vivo**, mostrando evolução e prática constante.

---

## 📝 Índice

### Aulas

1. [Aula 01 – Introdução ao Python](#aula-01---introdução-ao-python)
2. [Aula 02 – Manipulação de Strings](#aula-02---manipulação-de-strings)
3. [Aula 03 – Operadores em Python](#aula-03---operadores-em-python)
4. [Aula 04 – Estruturas de Controle em Python](#aula-04---estruturas-de-controle-em-python)
5. [Aula 05 – Estruturas de Dados em Python](#aula-05---estruturas-de-dados-em-python)

### Projetos

<!-- Futuras projetos serão adicionados aqui -->

---

# 📚 Aula 01 – Introdução ao Python

**Data:** *13/08/2025*

### 🧠 Objetivo

Aprender a **interagir com o terminal**, criar e manipular **variáveis básicas**, aplicar **convenções de código** e exibir informações de forma clara usando `print()` e `input()`.

### ⚡ Conceitos Principais

* `print()` → exibir mensagens no terminal.
* `input()` → receber dados do usuário.
* Tipos de dados: `str`, `int`, `float`, `bool`.
* Conversão de tipos: `int()`, `float()`, `str()`, `bool()`.
* Constantes → convenção em maiúsculas (`PI`).
* Convenção de nomes (snake\_case): `meu_nome_completo`.

### 💡 Exemplo Prático

```python
# Entrada de dados
usuario = input("Digite seu nome: ")
idade_input = int(input("Digite sua idade: "))

# Exibição
print(usuario, "tem", idade_input, "anos.")

# Conversão de tipos
numero_str = "10"
numero_int = int(numero_str)
numero_float = float(numero_int)
altura_str = str(1.78)
print(numero_str, numero_int, numero_float, altura_str)
```

---

# 📚 Aula 02 – Manipulação de Strings

**Data:** *13/08/2025*

### 🧠 Objetivo

Aprender a **trabalhar com texto**, manipulando **strings**, formatando saídas e utilizando métodos úteis para análise e transformação de textos.

### ⚡ Conceitos Principais

* **Strings** → textos delimitados por `'` ou `"`.
* **Concatenação** → juntar strings com `+`.
* **Repetição** → repetir strings com `*`.
* **Indexação** → acessar caracteres por índice (`0`, `-1`).
* **Fatiamento (Slicing)** → extrair partes da string `[início:fim]`.
* **Métodos úteis:**
  `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()`, `len()`, `.split()`,
  `.startswith()`, `.endswith()`, `.isalpha()`, `.isalnum()`, `.isdigit()`,
  `.isspace()`, `.strip()`, `.replace()`, `.count()`, `.find()`
* **f-strings** → formatar strings de forma legível e inserir variáveis diretamente.

---

### 💡 Exemplos Práticos

```python
# Entrada de dados
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = nome + " " + sobrenome
frase = "  Python é legal  "

# 1️⃣ Concatenar e repetir strings
print(nome_completo)       # Ex.: "Gabriel Rodrigues"
print("Python! " * 3)      # "Python! Python! Python! "

# 2️⃣ Indexação e fatiamento
print(frase[0])            # Primeiro caractere
print(frase[-1])           # Último caractere
print(frase[0:6])          # Primeiros 6 caracteres
print(frase[-5:])          # Últimos 5 caracteres

# 3️⃣ Métodos de transformação
print(frase.upper())       # Maiúsculas
print(frase.lower())       # Minúsculas
print(frase.title())       # Primeira letra de cada palavra maiúscula
print(frase.capitalize())  # Primeira letra maiúscula da frase
print(frase.swapcase())    # Inverte letra maiuscula por minuscula 

# 4️⃣ Métodos de análise
print(len(frase))          # Comprimento total da string
print(frase.split())       # Divide a string em palavras
print(frase.startswith("Python"))  # Verifica início
print(frase.endswith("legal"))     # Verifica final
print(frase.isalpha())     # Só letras? False
print(frase.isalnum())     # Só letras e números? False
print(frase.isdigit())     # Só números? False
print(frase.isspace())     # Só espaços? False

# 5️⃣ Limpeza e substituição
print(frase.strip())       # Remove espaços no início/fim
print(frase.replace(" ", "_"))  # Substitui espaços por "_"

# 6️⃣ Contagem e busca
print(frase.lower().count("a"))  # Conta a letra "a"
print(frase.find("legal"))       # Índice de início da palavra "legal"

# 7️⃣ f-strings
idade = int(input("Digite sua idade: "))
print(f"Meu nome é {nome_completo} e tenho {idade} anos.")
```

---

### 🧵 Resumo da Aula

* Strings podem ser **manipuladas** com métodos que transformam, analisam e formatam o texto.
* Métodos como `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.strip()`, `.replace()`, `.count()` e `.find()` são **essenciais para limpeza e análise de textos**.
* Podemos **concatenar**, **repetir**, **indexar** e **fatiar** strings para extrair ou organizar informações.
* **f-strings** permitem inserir variáveis diretamente dentro do texto de forma legível.

---

# 📚 Aula 03 – Operadores em Python

**Data:** *14/08/2025*

### 🧠 Objetivo

Aprender a **trabalhar com operadores em Python**, entendendo como realizar **operações matemáticas**, **comparações**, **atribuições**, **operações lógicas** e **verificações de identidade e associação**. Aplicar esses conceitos em **exemplos práticos**.

### ⚡ Conceitos Principais

1. **Operadores Aritméticos** → realizam cálculos matemáticos.

   * `+` → adição
   * `-` → subtração
   * `*` → multiplicação
   * `/` → divisão (float)
   * `//` → divisão inteira (int)
   * `%` → resto da divisão
   * `**` → exponenciação (potência)

2. **Operadores de Comparação** → comparam valores e retornam `True` ou `False`.

   * `==` → igual
   * `!=` → diferente
   * `>` → maior que
   * `<` → menor que
   * `>=` → maior ou igual
   * `<=` → menor ou igual

3. **Operadores Lógicos** → combinam expressões booleanas.

   * `and` → verdadeiro se ambos forem True
   * `or` → verdadeiro se pelo menos um for True
   * `not` → inverte o valor booleano

4. **Operadores de Atribuição** → modificam valores de variáveis.

   * `=` → atribuição simples
   * `+=` → soma e atribui
   * `-=` → subtração e atribui
   * `*=` → multiplicação e atribui
   * `/=` → divisão e atribui

5. **Operadores de Identidade** → verificam se duas variáveis apontam para o **mesmo objeto** na memória.

   * `is` → é o mesmo objeto
   * `is not` → não é o mesmo objeto

6. **Operadores de Associação** → verificam se um valor está **presente em uma sequência** (listas, tuplas, strings).

   * `in` → está presente
   * `not in` → não está presente

---

### 💡 Exemplos Práticos

```python
# Operadores Aritméticos
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Operadores de Comparação
x, y = 5, 8
print(x == y, x != y, x > y, x < y, x >= y, x <= y)

# Operadores Lógicos
p, q = True, False
print(p and q, p or q, not p)

# Operadores de Atribuição
num = 10
num += 5
num *= 2
num /= 4
print(num)

# Operadores de Identidade
list1 = [1,2,3]; list2 = list1; list3 = [1,2,3]
print(list1 is list2, list1 is list3, list1 is not list3)

# Operadores de Associação
frutas = ["maçã","banana","laranja"]
print("banana" in frutas, "uva" in frutas, "uva" not in frutas)

# Exercício Prático
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Divisão inteira:", num1 // num2 if num2 != 0 else "Indefinido")
print("Divisão:", num1 / num2 if num2 != 0 else "Indefinido")
print("num1 > num2?", num1 > num2)
print("num1 < num2?", num1 < num2)
print("num1 == num2?", num1 == num2)
print("(num1 > 0) and (num2 > 0):", (num1 > 0) and (num2 > 0))
```

---

### 🧵 Resumo da Aula

* Operadores permitem **manipular números e variáveis**, realizar **comparações**, combinar **expressões booleanas** e atualizar valores de forma prática.
* **Operadores de identidade e associação** ajudam a verificar **objetos em memória** ou **elementos em sequências**.
* Aplicar operadores em **exercícios práticos** ajuda a fixar a lógica e entender **como Python avalia expressões**.

---

# 📚 Aula 04 – Estruturas de Controle em Python

**Data:** *14/08/2025*

### 🧠 Objetivo

Aprender a **controlar o fluxo do programa** em Python, utilizando **decisões condicionais**, **laços de repetição**, **comandos de controle de fluxo** e **estruturas aninhadas**. Aplicar esses conceitos em **exemplos práticos** e exercícios.

### ⚡ Conceitos Principais

1. **Estruturas Condicionais** → executam blocos de código conforme condições.

   * `if` → executa se a condição for verdadeira.
   * `elif` → executa se a condição anterior for falsa e esta for verdadeira.
   * `else` → executa se todas as condições anteriores forem falsas.

2. **Estruturas de Repetição** → executam blocos de código várias vezes.

   * `while` → repete enquanto a condição for verdadeira.
   * `for` → itera sobre sequências (listas, strings, ranges).

3. **Estruturas de Controle de Fluxo** → alteram o fluxo normal do programa.

   * `break` → interrompe o loop imediatamente.
   * `continue` → pula a iteração atual e continua no loop.
   * `pass` → comando nulo; não faz nada, mas é sintaticamente necessário.

4. **Estruturas Aninhadas** → colocar uma estrutura de controle dentro de outra.

---

### 💡 Exemplos Práticos

```python
# 1️⃣ Estruturas Condicionais
x = 10
if x > 0:
    print("x é positivo")
elif x < 0:
    print("x é negativo")
else:
    print("x é zero")

# 2️⃣ Loop while
count = 0
while count < 5:
    print("Contagem:", count)
    count += 1

# 3️⃣ Loop for
for i in range(5):
    print("Iteração:", i)

# 4️⃣ Controle de Fluxo
for i in range(5):
    if i == 3:
        break
    print("Valor antes do break:", i)

for i in range(5):
    if i == 2:
        continue
    print("Valor após o continue:", i)

for i in range(3):
    if i == 1:
        pass
    print("Valor com pass:", i)

# 5️⃣ Estruturas Aninhadas
for i in range(3):
    print("Loop externo, i =", i)
    for j in range(2):
        print("   Loop interno, j =", j)

# 6️⃣ Exercício Prático
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

print("Números de 0 até", num, ":")
for i in range(num + 1):
    print(i)
```

---

### 🧵 Resumo da Aula

* **Condicionais (`if`, `elif`, `else`)** permitem executar diferentes ações conforme condições.
* **Laços de repetição (`for`, `while`)** repetem blocos de código e podem ser controlados por **`break`**, **`continue`** e **`pass`**.
* **Estruturas aninhadas** possibilitam criar lógica mais complexa combinando loops e condicionais.
* Aplicar essas estruturas em exercícios práticos ajuda a **entender o fluxo do programa e a tomada de decisões automáticas**.

---

# 📚 Aula 05 – Estruturas de Dados em Python

**Data:** *14/08/2025*

### 🧠 Objetivo

Aprender a **armazenar e organizar informações** usando as principais **estruturas de dados em Python**, incluindo **listas, tuplas, dicionários e conjuntos**. Aplicar os conceitos em **exercícios práticos** com interação do usuário.

### ⚡ Conceitos Principais

1. **Listas** → coleções **ordenadas e mutáveis** de itens.

   * `append()` → adiciona um item no final.
   * `remove()` → remove um item específico.
   * `len()` → retorna o tamanho da lista.
   * Indexação → acessar itens por posição: `lista[0]`.

2. **Tuplas** → coleções **ordenadas e imutáveis** de itens.

   * Indexação → acessar itens por posição: `tupla[0]`.
   * `len()` → retorna o tamanho da tupla.

3. **Dicionários** → coleções **não ordenadas de pares chave-valor**.

   * Acesso → `dicionario[chave]`.
   * Atualizar → `dicionario[chave] = valor`.
   * Adicionar → `dicionario[nova_chave] = valor`.
   * Métodos úteis → `keys()`, `values()`.

4. **Conjuntos (Sets)** → coleções **não ordenadas de itens únicos**.

   * `add()` → adiciona item.
   * `remove()` → remove item.
   * Operadores de associação → `in`, `not in`.
   * `len()` → retorna o tamanho do conjunto.

---

### 💡 Exemplos Práticos

```python
# Listas
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
frutas.remove("banana")
print(frutas)
print(frutas[0], len(frutas))

# Tuplas
coordenadas = (10.0, 20.0)
print(coordenadas, coordenadas[0], len(coordenadas))

# Dicionários
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
pessoa["idade"] = 31
pessoa["profissão"] = "Engenheira"
print(pessoa, list(pessoa.keys()), list(pessoa.values()))

# Conjuntos
numeros = {1,2,3,4,5}
numeros.add(6)
numeros.remove(3)
print(numeros, 4 in numeros, len(numeros))

# Exercício prático – Lista de frutas do usuário
frutas_usuario = []
while True:
    fruta = input("Digite o nome de uma fruta (ou 'sair' para terminar): ")
    if fruta.lower() == "sair":
        break
    frutas_usuario.append(fruta)
print("Frutas inseridas:", frutas_usuario)

# Exercício prático – Atualizar ano de um livro
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
novo_ano = int(input("Digite o novo ano de publicação: "))
livro["ano"] = novo_ano
print("Informações atualizadas:", livro)
```

---

### 🧵 Resumo da Aula

* **Listas** → úteis para coleções **mutáveis** e ordenadas de itens.
* **Tuplas** → ideais quando os dados **não devem ser alterados**.
* **Dicionários** → perfeitos para **armazenar informações relacionadas por chave**.
* **Conjuntos** → ótimos para garantir **itens únicos** e realizar operações de associação.
* Exercícios práticos ajudam a **interagir com dados**, atualizar informações e consolidar o aprendizado.

---
