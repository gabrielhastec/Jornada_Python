# Aula 03 - Operadores em Python
# Nesta aula, vamos explorar os principais operadores em Python e como usá-los.

# 1. Operadores Aritméticos
# Operadores que realizam operações matemáticas básicas.
a = 10
b = 3
print("1. Operadores Aritméticos:")
print("   - Adição (a + b):", a + b)  # Soma
print("   - Subtração (a - b):", a - b)  # Subtração
print("   - Multiplicação (a * b):", a * b) # Multiplicação 
print("   - Divisão (a / b):", a / b)  # Divisão (resultado float)
print("   - Divisão Inteira (a // b):", a // b)  # Divisão inteira (resultado int)
print("   - Módulo (a % b):", a % b)  # Resto da divisão
print("   - Exponenciação (a ** b):", a ** b)  # Potência
print()

# 2. Operadores de Comparação
# Operadores que comparam dois valores e retornam um booleano (True/False).
x = 5
y = 8
print("2. Operadores de Comparação:")
print("   - Igual (x == y):", x == y)  # Verifica se x é igual a y
print("   - Diferente (x != y):", x != y)  # Verifica se x é diferente de y
print("   - Maior que (x > y):", x > y)  # Verifica se x é maior que y
print("   - Menor que (x < y):", x < y)  # Verifica se x é menor que y
print("   - Maior ou igual (x >= y):", x >= y)  # Verifica se x é maior ou igual a y
print("   - Menor ou igual (x <= y):", x <= y)  # Verifica se x é menor ou igual a y
print()

# 3. Operadores Lógicos
# Operadores que combinam expressões booleanas.
p = True
q = False
print("3. Operadores Lógicos:")
print("   - AND (p and q):", p and q)  # Verdadeiro se ambos forem True
print("   - OR (p or q):", p or q)  # Verdadeiro se pelo menos um for True
print("   - NOT (not p):", not p)  # Inverte o valor booleano
print()

# 4. Operadores de Atribuição
# Operadores que atribuem valores a variáveis.
num = 10
print("4. Operadores de Atribuição:")
print("   - Atribuição simples (num = 10):", num)
num += 5  # Equivalente a num = num + 5
print("   - Adição e atribuição (num += 5):", num)
num -= 3  # Equivalente a num = num - 3
print("   - Subtração e atribuição (num -= 3):", num)
num *= 2  # Equivalente a num = num * 2
print("   - Multiplicação e atribuição (num *= 2):", num)
num /= 4  # Equivalente a num = num / 4
print("   - Divisão e atribuição (num /= 4):", num)
print()

# 5. Operadores de Identidade
# Verificam se duas variáveis apontam para o mesmo objeto na memória.
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("5. Operadores de Identidade:")
print("   - is (list1 is list2):", list1 is list2)  # True, pois list2 aponta para o mesmo objeto que list1
print("   - is (list1 is list3):", list1 is list3)  # False, pois list3 é um objeto diferente, apesar de ter o mesmo conteúdo
print("   - is not (list1 is not list3):", list1 is not list3)  # True, pois list1 e list3 são objetos diferentes
print()

# 6. Operadores de Associação
# Verificam se um valor está presente em uma sequência (como listas, tuplas ou strings).
frutas = ["maçã", "banana", "laranja"]
print("6. Operadores de Associação:")
print("   - in ('banana' in frutas):", "banana" in frutas)  # True, pois 'banana' está na lista
print("   - in ('uva' in frutas):", "uva" in frutas)  # False, pois 'uva' não está na lista
print("   - not in ('uva' not in frutas):", "uva" not in frutas)  # True, pois 'uva' não está na lista
print()

## Exercício Prático
# Peça ao usuário para inserir dois números e mostre o resultado de várias operações usando os operadores aprendidos.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Resultados das operações:")
print("   - Soma (num1 + num2):", num1 + num2)  # Adição
print("   - Subtração (num1 - num2):", num1 - num2) # Subtração
print("   - Multiplicação (num1 * num2):", num1 * num2) # Multiplicação
print("   - Divisão inteira (num1 // num2):", num1 // num2 if num2 != 0 else "Indefinido (divisão por zero)")  # Divisão inteira com verificação de zero
print("   - Divisão (num1 / num2):", num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)") # Divisão com verificação de zero

# Usando operadores de comparação e lógicos
print("   - num1 após num1 += 10:", num1)   # Mostra num1 atualizado
print("   - num2 após num2 *= 2:", num2)    # Mostra num2 atualizado
print("   - num1 é maior que num2?", num1 > num2)   # Maior que
print("   - num1 é menor que num2?", num1 < num2)   # Menor que
print("   - num1 é igual a num2?", num1 == num2)    # Igual
print("   - num1 é diferente de num2?", num1 != num2)   # Diferente
print("   - num1 é maior ou igual a num2?", num1 >= num2)  # Maior ou igual
print("   - num1 é menor ou igual a num2?", num1 <= num2)  # Menor ou igual
print("   - (num1 > 0) and (num2 > 0):", (num1 > 0) and (num2 > 0))  # Ambos positivos
print("   - (num1 > 0) or (num2 > 0):", (num1 > 0) or (num2 > 0)) # Pelo menos um positivo

# Usando operador de atribuição composto
num1 += 10  # Adiciona 10 a num1
num2 *= 2   # Multiplica num2 por 2
print("   - num1 += 5:", (num1 := num1 + 5))    # Atribuição com expressão
print("   - num2 *= 2:", (num2 := num2 * 2))

# Verifica associação em uma lista
frutas = ["maçã", "banana", "laranja"]
print("   - 'banana' in frutas?", "banana" in frutas)
print("   - 'maçã' in frutas?", "maçã" in frutas)   
print("   - 'uva' not in frutas?", "uva" not in frutas)
print()
