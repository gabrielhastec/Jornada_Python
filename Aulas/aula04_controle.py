# Aula 04 - Estruturas de Controle em Python
# Nesta aula, vamos explorar as principais estruturas de controle em Python, que nos permitem tomar decisões e repetir ações no código.

# 1. Estruturas Condicionais
# As estruturas condicionais permitem executar diferentes blocos de código com base em condições.
print("1. Estruturas Condicionais:")
x = 10
if x > 0:   # Verifica se x é maior que 0
    print("   - x é positivo")
elif x < 0: # Verifica se x é menor que 0
    print("   - x é negativo")
else:   # Se nenhuma das condições anteriores for verdadeira
    print("   - x é zero")
print()

# 2. Estruturas de Repetição
# As estruturas de repetição permitem executar um bloco de código várias vezes.
print("2. Estruturas de Repetição:")

# 2.1. Loop while
# O loop while executa enquanto a condição for verdadeira.
count = 0
while count < 5:    # Continua enquanto count for menor que 5
    print("   - Contagem:", count)
    count += 1  # Incrementa count em 1
print()

# 2.3. Loop for percorrendo uma string
# O loop for percorre cada caractere de uma string.
string = "Python"
for char in string:  # Itera sobre cada caractere na string
    print("   - Caractere:", char)
print()

# 2.4. Loop for com range
# O loop for itera sobre uma sequência de números gerada pela função range.
print("2.2. Loop for com range:")
for i in range(5):  # Itera de 0 a 4
    print("   - Iteração:", i)
print()

# 2.5. Loop for com lista
# Podemos iterar diretamente sobre os elementos de uma lista.
lista = ['a', 'b', 'c']
for letra in lista:  # Itera sobre cada letra na lista
    print("   - Letra:", letra)
print()

# 3. Estruturas de Controle de Fluxo
# As estruturas de controle de fluxo permitem alterar o fluxo normal do programa.
print("3. Estruturas de Controle de Fluxo:")

# 3.1. break
# O break interrompe o loop imediatamente.
for i in range(5):
    if i == 3:  # Se i for igual a 3, interrompe o loop
        break   
    print("   - Valor antes do break:", i)  
print("   - Loop interrompido pelo break")

# 3.2. continue
# O continue pula a iteração atual e continua com a próxima.
for i in range(5):
    if i == 2:  # Se i for igual a 2, pula esta iteração
        continue
    print("   - Valor após o continue:", i)
print("   - Loop continuado pelo continue")

# 3.3. pass
# O pass é um comando nulo, usado quando uma declaração é necessária sintaticamente, mas não se deseja executar nenhuma ação.
for i in range(3):
    if i == 1:  # Se i for igual a 1, não faz nada
        pass  # Apenas passa para a próxima iteração
    print("   - Valor com pass:", i)
print("   - Loop executado com pass")
print()

# 4. Estruturas Aninhadas
# Podemos aninhar estruturas de controle dentro de outras.
print("4. Estruturas Aninhadas:")
for i in range(3):  # Loop externo
    print("   - Loop externo, i =", i)
    for j in range(2):  # Loop interno
        print("      - Loop interno, j =", j)
print("   - Estruturas aninhadas concluídas")
print()

# Exercício Prático
# Peça ao usuário para inserir um número e verifique se é par ou ímpar, além de imprimir os números de 0 até o número inserido.
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("   - O número é par.")
else:
    print("   - O número é ímpar.")
print("   - Números de 0 até", num, ":")
for i in range(num + 1):
    print("      -", i)
print("   - Fim do exercício prático")
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
