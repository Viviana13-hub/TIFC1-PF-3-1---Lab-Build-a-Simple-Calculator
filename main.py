# Programa básico (necesario para calificación automática)

num1 = float(input())
num2 = float(input())

resultado = num1 + num2

print(resultado)

print("--- CALCULADORA ---")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

op = input("Elige opción: ")

if op == "1":
    print("Resultado:", num1 + num2)
elif op == "2":
    print("Resultado:", num1 - num2)
elif op == "3":
    print("Resultado:", num1 * num2)
elif op == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("No se puede dividir por cero")