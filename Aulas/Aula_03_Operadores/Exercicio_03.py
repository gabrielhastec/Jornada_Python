# Exercício 03 - Operadores em Python
# Gabriel Rodrigues

print("=== Exercício 03 - Operadores ===")

# Solicitar dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n--- Operadores Aritméticos ---")
print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Divisão:", num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)")
print("Divisão inteira:", num1 // num2 if num2 != 0 else "Indefinido (divisão por zero)")
print("Módulo:", num1 % num2 if num2 != 0 else "Indefinido (divisão por zero)")
print("Exponenciação:", num1 ** num2)

print("\n--- Operadores de Comparação ---")
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)

print("\n--- Operadores Lógicos ---")
print("(num1 > 0) and (num2 > 0):", (num1 > 0) and (num2 > 0))
print("(num1 > 0) or (num2 > 0):", (num1 > 0) or (num2 > 0))
print("not (num1 > 0):", not (num1 > 0))

print("\n--- Operadores de Atribuição ---")
num1 += 10
num2 *= 2
print("num1 += 10:", num1)
print("num2 *= 2:", num2)

print("\n--- Operadores de Associação ---")
frutas = ["maçã", "banana", "laranja"]
print("'banana' in frutas?", "banana" in frutas)
print("'uva' not in frutas?", "uva" not in frutas)
