import re

def clasificar_entrada(entrada: str) -> str:
    if entrada.strip() == "":
        return "vacía o solo espacios"
    elif re.fullmatch(r"-?\d+\.\d+", entrada):
        return "número decimal"
    elif re.fullmatch(r"-?\d+", entrada):
        return "entero válido"
    elif re.search(r"[a-zA-Z]", entrada):
        return "texto alfabético"
    elif re.search(r"[^\w\s\-\.]", entrada):
        return "caracteres especiales"
    else:
        return "entrada no reconocida"

def iniciar_programa():
    print("\n📌 Bienvenido al validador interactivo de enteros")
    print("🔢 Ingrese enteros cuando quiera. Escriba 'salir' para terminar o 'resumen' para ver lo que ha ingresado.\n")

    valores_validos = []
    historial_completo = []

    while True:
        entrada = input("📝 Ingresa un dato: ").strip()
        historial_completo.append(entrada)

        # Comandos especiales
        if entrada.lower() == "salir":
            print("👋 Programa finalizado por el usuario.")
            break
        elif entrada.lower() == "resumen":
            print("\n📋 RESUMEN DE LA SESIÓN")
            print("✔️ Enteros válidos ingresados:", valores_validos if valores_validos else "Ninguno aún")
            print("📦 Total de entradas:", len(historial_completo))
            print("🧾 Entradas completas:", historial_completo)
            print("-" * 40)
            continue

        tipo = clasificar_entrada(entrada)

        if tipo == "entero válido":
            numero = int(entrada)
            valores_validos.append(numero)
            print(f"✅ ¡Correcto! Has ingresado el entero: {numero}\n")
        else:
            print(f"🚫 Entrada rechazada: '{entrada}' es {tipo}. Por favor, ingresa un número entero.\n")

    print("\n🎉 ¡Gracias por usar el validador interactivo!")

# Ejecutar el programa
if __name__ == "__main__":
    iniciar_programa()
