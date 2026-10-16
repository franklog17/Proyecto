# Constante de módulo para el tamaño del arreglo
CAPACIDAD_MAX = 10


def registrar_en_arreglo(arreglo, contador, monto):
    """Guarda un monto en la posición actual del arreglo si hay espacio."""
    if contador < CAPACIDAD_MAX:
        arreglo[contador] = monto
        return contador + 1
    else:
        print(" Error: El arreglo está lleno. No caben más registros.")
        return contador


def ver_balance(balance):
    """Devuelve el monto formateado como texto con 2 decimales y signo $."""
    return f"${balance:.2f}"


def pedir_monto_valido(mensaje):
    """Asegura mediante un ciclo while que el monto sea mayor a cero."""
    monto = float(input(mensaje))
    while monto <= 0:
        print(" Error: El monto debe ser un número mayor a 0.")
        monto = float(input(mensaje))
    return monto


def mostrar_arreglo(arreglo, cantidad, tipo):
    """Recorre el arreglo mediante un ciclo for hasta la cantidad ocupada."""
    print(f"\n--- HISTORIAL DE {tipo.upper()}S ---")
    if cantidad == 0:
        print(f"No hay {tipo}s registrados.")
    else:
        for i in range(cantidad):
            print(f"Posición [{i}]: ${arreglo[i]:.2f}")


def calcular_suma_arreglo(arreglo, cantidad):
    """Suma los elementos válidos guardados en el arreglo."""
    total = 0.0
    for i in range(cantidad):
        total += arreglo[i]
    return total


# --- PROGRAMA PRINCIPAL ---

usuario = input("¿Cuál es tu nombre? ")

# Definición de arreglos estáticos con tamaño fijo
ingresos = [0.0] * CAPACIDAD_MAX
gastos = [0.0] * CAPACIDAD_MAX

# Contadores de elementos ocupados en cada arreglo
cant_ingresos = 0
cant_gastos = 0

opcion = ""

while opcion != "5":
    print(f"\n=== GESTOR DE FINANZAS DE {usuario.upper()} ===")
    print("1. Registrar un ingreso")
    print("2. Registrar un gasto")
    print("3. Ver balance actual")
    print("4. Ver historial (Arreglos)")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        if cant_ingresos < CAPACIDAD_MAX:
            monto = pedir_monto_valido("¿Cuánto dinero ganaste? $")
            cant_ingresos = registrar_en_arreglo(
                ingresos, cant_ingresos, monto
            )
            total_ing = calcular_suma_arreglo(ingresos, cant_ingresos)
            total_gas = calcular_suma_arreglo(gastos, cant_gastos)
            print(f" Registrado. Balance: {ver_balance(total_ing - total_gas)}")
        else:
            print(" Capacidad máxima de ingresos alcanzada.")

    elif opcion == "2":
        if cant_gastos < CAPACIDAD_MAX:
            monto = pedir_monto_valido("¿Cuánto dinero gastaste? $")
            total_ing = calcular_suma_arreglo(ingresos, cant_ingresos)
            total_gas = calcular_suma_arreglo(gastos, cant_gastos)

            if monto > (total_ing - total_gas):
                print(" ¡Advertencia! Este gasto supera tu saldo actual.")

            cant_gastos = registrar_en_arreglo(gastos, cant_gastos, monto)
            total_gas = calcular_suma_arreglo(gastos, cant_gastos)
            print(f" Registrado. Balance: {ver_balance(total_ing - total_gas)}")
        else:
            print(" Capacidad máxima de gastos alcanzada.")

    elif opcion == "3":
        total_ing = calcular_suma_arreglo(ingresos, cant_ingresos)
        total_gas = calcular_suma_arreglo(gastos, cant_gastos)
        print(f"\n Tu saldo actual es: {ver_balance(total_ing - total_gas)}")

    elif opcion == "4":
        mostrar_arreglo(ingresos, cant_ingresos, "ingreso")
        mostrar_arreglo(gastos, cant_gastos, "gasto")

    elif opcion == "5":
        print(f"\n¡Hasta luego, {usuario}! Gracias por usar el gestor.")

    else:
        print(" Opción no válida. Por favor, elige un número del 1 al 5.")