
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

