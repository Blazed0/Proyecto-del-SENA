def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

numero = int(input("Ingresa un número entero no negativo: "))

if numero < 0:
    print("Por favor, ingresa un número entero no negativo.")
else:
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")