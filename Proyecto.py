# Constantes del menú a nivel de módulo
OPCION_INGRESO = "1"
OPCION_GASTO = "2"
OPCION_BALANCE = "3"
OPCION_HISTORIAL = "4"
OPCION_ESTADISTICAS = "5"
OPCION_SALIR = "6"


def registrar_transaccion(matriz, monto, tipo):
    """Agrega un sub-arreglo [monto, tipo] a la matriz de transacciones."""
    matriz.append([monto, tipo])


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


def calcular_total_por_tipo(matriz, tipo_buscado):
    """Suma los montos de una matriz bidimensional filtrando por tipo."""
    total = 0.0
    for i in range(len(matriz)):
        if matriz[i][1] == tipo_buscado:
            total += matriz[i][0]
    return total


def mostrar_historial(matriz, tipo_buscado):
    """Imprime el listado numerado de elementos de un tipo específico."""
    print(f"\n--- HISTORIAL DE {tipo_buscado.upper()}S ---")
    contador = 0
    
    for i in range(len(matriz)):
        if matriz[i][1] == tipo_buscado:
            contador += 1
            print(f"{contador}. ${matriz[i][0]:.2f}")
            
    if contador == 0:
        print(f"No hay {tipo_buscado}s registrados.")


def calcular_estadisticas(matriz, tipo_buscado):
    """Calcula suma, promedio, máximo y mínimo usando índices de arreglos."""
    total = 0.0
    contador = 0
    maximo = -1.0 
    minimo = float('inf')

    for i in range(len(matriz)):
        if matriz[i][1] == tipo_buscado:
            monto = matriz[i][0]
            total += monto
            contador += 1
            
            if monto > maximo:
                maximo = monto
            if monto < minimo:
                minimo = monto

    if contador == 0:
        print(f"\nNo hay datos registrados para estadísticas de "
              f"{tipo_buscado}.")
        return

    promedio = total / contador

    print(f"\n--- ESTADÍSTICAS DE {tipo_buscado.upper()}S ---")
    print(f"Total acumulado: ${total:.2f}")
    print(f"Promedio por registro: ${promedio:.2f}")
    print(f"Mayor {tipo_buscado}: ${maximo:.2f}")
    print(f"Menor {tipo_buscado}: ${minimo:.2f}")


def main():
    """Función principal que ejecuta el gestor de finanzas."""
    usuario = input("¿Cuál es tu nombre? ")

    # Arreglo bidimensional (matriz) para el historial
    transacciones = []
    opcion = ""

    while opcion != OPCION_SALIR:
        print(f"\n=== GESTOR DE FINANZAS DE {usuario.upper()} ===")
        print(f"{OPCION_INGRESO}. Registrar un ingreso")
        print(f"{OPCION_GASTO}. Registrar un gasto")
        print(f"{OPCION_BALANCE}. Ver balance actual")
        print(f"{OPCION_HISTORIAL}. Ver historial de movimientos")
        print(f"{OPCION_ESTADISTICAS}. Ver estadísticas del día")
        print(f"{OPCION_SALIR}. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == OPCION_INGRESO:
            monto = pedir_monto_valido("¿Cuánto dinero ganaste? $")
            registrar_transaccion(transacciones, monto, "ingreso")
            
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            
            balance = ingresos - gastos
            print(f" Ingreso registrado. Balance: {ver_balance(balance)}")

        elif opcion == OPCION_GASTO:
            monto = pedir_monto_valido("¿Cuánto dinero gastaste? $")
            
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance_actual = ingresos - gastos

            if monto > balance_actual:
                print(" ¡Advertencia! El gasto supera tu saldo disponible.")

            registrar_transaccion(transacciones, monto, "gasto")
            balance = balance_actual - monto
            print(f" Gasto registrado. Balance: {ver_balance(balance)}")

        elif opcion == OPCION_BALANCE:
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance = ingresos - gastos
            print(f"\n Tu saldo actual es: {ver_balance(balance)}")

        elif opcion == OPCION_HISTORIAL:
            mostrar_historial(transacciones, "ingreso")
            mostrar_historial(transacciones, "gasto")

        elif opcion == OPCION_ESTADISTICAS:
            calcular_estadisticas(transacciones, "ingreso")
            calcular_estadisticas(transacciones, "gasto")

        elif opcion == OPCION_SALIR:
            print(f"\n¡Hasta luego, {usuario}! Gracias por usar el gestor.")

        else:
            print(" Opción no válida. Por favor, elige un número del 1 al 6.")


# Ejecución del programa principal
if __name__ == "__main__":
    main()