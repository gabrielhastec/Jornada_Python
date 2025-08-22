
# 📚 Aula 01 – Introdução ao Python

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python\&logoColor=white) ![Nível](https://img.shields.io/badge/Nível-Básico-green) ![Status](https://img.shields.io/badge/Status-Concluída-brightgreen)

**Autor:** Gabriel Rodrigues
**Data:** 13/08/2025

---

## 🧠 Objetivo da Aula

Nesta aula você aprenderá:

* Como imprimir mensagens no terminal
* Criação e manipulação de variáveis
* Tipos de dados básicos: `str`, `int`, `float` e `bool`
* Convenções de nomenclatura (snake\_case)
* Uso de constantes
* Entrada de dados com `input()`
* Conversão de tipos (`int()`, `float()`, `str()`, `bool()`)
* Verificação de tipos com `type()`
* Uso de comentários

---

## ⚡ Conteúdos e Exemplos

### 1️⃣ Imprimindo mensagens

```python
print("Olá, mundo!")
print("Estou aprendendo Python!\n")
```

### 2️⃣ Variáveis e tipos de dados

```python
nome = "Gabriel"
idade = 25
altura = 1.78
estudando = True

print(nome, idade, altura, estudando)
```

### 3️⃣ Constantes e snake\_case

```python
PI = 3.14159
meu_nome_completo = "Gabriel Rodrigues"
idade_usuario = 25
```

### 4️⃣ Entrada de dados

```python
nome_completo = input("Digite seu nome completo: ")
idade_input = input("Digite sua idade: ")
```

### 5️⃣ Conversão de tipos

```python
numero_int = int("10")
numero_float = float(numero_int)
altura_str = str(altura)
print(bool(0), bool(1), bool("Python"), bool(""))
```

### 6️⃣ Verificação de tipos

```python
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))
```

---

## 📝 Exercício 01 – Fixação

**Objetivo:** Fixar o que foi aprendido nesta aula, praticando variáveis, tipos de dados, entrada de informações e conversão de tipos.

### Instruções

1. Crie variáveis para armazenar:

   * Seu nome (string)
   * Sua idade (inteiro)
   * Sua altura (float)
   * Se você está estudando Python (booleano)

2. Exiba todas as informações usando `print()`

3. Solicite ao usuário:

   * Nome completo
   * Idade

4. Converta a idade digitada para inteiro

5. Crie uma constante `PI = 3.14` e exiba

6. Converta a altura para string e exiba o tipo antes e depois

7. Teste a conversão de valores para booleano: `0`, `1`, `"Python"`, `""`

8. Verifique o tipo de todas as variáveis usando `type()`

💡 **Dica:** Utilize comentários e a convenção **snake\_case**.

[📂 Abrir Exercício 01](./Exercicio_01.py) ✅

---

### 🧵 Resumo da Aula

* Impressão de mensagens e entrada de dados são essenciais para interagir com o usuário
* Variáveis armazenam dados e cada tipo de dado tem suas regras
* Conversões e verificação de tipos ajudam a garantir que o programa funcione corretamente
* Constantes e convenções de nomenclatura facilitam a leitura e manutenção do código
