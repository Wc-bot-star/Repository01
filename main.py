def es_primo(n):
    # Si el número es menor o igual a 1, no es primo
    if n <= 1:
        return False
    # Verificamos divisores posibles desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Si se encuentra un divisor, no es primo
    return True  # Si no se encontró divisor, es primo

# Prueba del código
numero = int(input("Ingresa un número para verificar si es primo: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
