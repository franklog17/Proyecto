# Descripción: Gestor de finanzas interactivo con soporte de listas
# para almacenar e analizar el historial de transacciones.


def registrar_monto(lista_destino, monto):
    """Agrega un monto validado a la lista de transacciones dada."""
    lista_destino.append(monto)


def ver_balance(balance):
    """Devuelve el monto formateado como texto con 2 decimales y signo $."""
    return f"${balance:.2f}"


def pedir_monto_valido(mensaje):
    """Asegura mediante un ciclo mientras que el monto sea mayor a cero."""
    monto = float(input(mensaje))
    while monto <= 0:
        print(" Error: El monto debe ser un número mayor a 0.")
        monto = float(input(mensaje))
    return monto


def mostrar_historial(lista, tipo):
    """Imprime el listado numerado de elementos de una lista."""
    print(f"\n--- HISTORIAL DE {tipo.upper()}S ---")
    if not lista:
        print(f"No hay {tipo}s registrados.")
    else:
        for i in range(len(lista)):
            print(f"{i + 1}. ${lista[i]:.2f}")


def calcular_estadisticas(lista, tipo):
    """Muestra la suma, promedio, máximo y mínimo de una lista."""
    if not lista:
        print(f"\nNo hay datos registrados para estadísticas de {tipo}.")
        return

    total = sum(lista)
    promedio = total / len(lista)
    maximo = max(lista)
    minimo = min(lista)

    print(f"\n--- ESTADÍSTICAS DE {tipo.upper()}S ---")
    print(f"Total acumulado: ${total:.2f}")
    print(f"Promedio por registro: ${promedio:.2f}")
    print(f"Mayor {tipo}: ${maximo:.2f}")
    print(f"Menor {tipo}: ${minimo:.2f}")


# --- PROGRAMA PRINCIPAL ---

usuario = input("¿Cuál es tu nombre? ")

# Inicialización de arreglos/listas para el historial
ingresos = []
gastos = []

opcion = ""

while opcion != "6":
    print(f"\n=== GESTOR DE FINANZAS DE {usuario.upper()} ===")
    print("1. Registrar un ingreso")
    print("2. Registrar un gasto")
    print("3. Ver balance actual")
    print("4. Ver historial de movimientos")
    print("5. Ver estadísticas del día")
    print("6. Salir")

    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        monto = pedir_monto_valido("¿Cuánto dinero ganaste? $")
        registrar_monto(ingresos, monto)
        balance = sum(ingresos) - sum(gastos)
        print(f" Ingreso registrado. Balance: {ver_balance(balance)}")

    elif opcion == "2":
        monto = pedir_monto_valido("¿Cuánto dinero gastaste? $")
        balance_actual = sum(ingresos) - sum(gastos)

        if monto > balance_actual:
            print(" ¡Advertencia! El gasto supera tu saldo disponible.")

        registrar_monto(gastos, monto)
        balance = sum(ingresos) - sum(gastos)
        print(f" Gasto registrado. Balance: {ver_balance(balance)}")

    elif opcion == "3":
        balance = sum(ingresos) - sum(gastos)
        print(f"\n Tu saldo actual es: {ver_balance(balance)}")

    elif opcion == "4":
        mostrar_historial(ingresos, "ingreso")
        mostrar_historial(gastos, "gasto")

    elif opcion == "5":
        calcular_estadisticas(ingresos, "ingreso")
        calcular_estadisticas(gastos, "gasto")

    elif opcion == "6":
        print(f"\n¡Hasta luego, {usuario}! Gracias por usar el gestor.")

    else:
        print(" Opción no válida. Por favor, elige un número del 1 al 6.")