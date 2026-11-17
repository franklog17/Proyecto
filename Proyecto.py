"""Gestor de finanzas personales - Avance 8 (Manipulación de cadenas)."""

OPCION_INGRESO = "1"
OPCION_GASTO = "2"
OPCION_BALANCE = "3"
OPCION_HISTORIAL = "4"
OPCION_BUSCAR = "5"
OPCION_SALIR = "6"


def registrar_transaccion(matriz, monto, tipo, descripcion):
    """Agrega un sub-arreglo con monto, tipo y descripción a la matriz."""
    matriz.append([monto, tipo, descripcion])


def ver_balance(balance):
    """Devuelve el monto formateado como texto con 2 decimales."""
    return f"${balance:.2f}"


def pedir_monto_valido(mensaje):
    """Asegura mediante un ciclo while que el monto sea mayor a cero."""
    monto = float(input(mensaje))
    while monto <= 0:
        print("Error: El monto debe ser mayor a 0.")
        monto = float(input(mensaje))
    return monto


def pedir_texto_valido(mensaje):
    """Asegura que la cadena ingresada no esté vacía usando strip."""
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: El texto no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto


def calcular_total_por_tipo(matriz, tipo_buscado):
    """Suma los montos de la matriz filtrando por tipo."""
    total = 0.0
    for i in range(len(matriz)):
        if matriz[i][1] == tipo_buscado:
            total += matriz[i][0]
    return total


def mostrar_historial(matriz, tipo_buscado):
    """Imprime el listado formateado de elementos de un tipo específico."""
    print(f"\n--- HISTORIAL DE {tipo_buscado.upper()}S ---")
    contador = 0
    for i in range(len(matriz)):
        if matriz[i][1] == tipo_buscado:
            contador += 1
            monto_str = f"${matriz[i][0]:.2f}"
            # Manipulación de cadenas para presentación (capitalize)
            desc = matriz[i][2].capitalize()
            print(f"{contador}. {monto_str} - {desc}")
    if contador == 0:
        print(f"No hay {tipo_buscado}s registrados.")


def buscar_transacciones(matriz, palabra_clave):
    """Busca y muestra transacciones que contienen la palabra clave."""
    palabra = palabra_clave.strip().lower()
    print(f"\n--- RESULTADOS DE BÚSQUEDA: '{palabra_clave}' ---")
    encontrados = 0
    for i in range(len(matriz)):
        desc = matriz[i][2].lower()
        # Uso de cadenas: verificación de subcadena con 'in'
        if palabra in desc:
            encontrados += 1
            tipo = matriz[i][1]
            monto = f"${matriz[i][0]:.2f}"
            descripcion_limpia = matriz[i][2].capitalize()
            print(f"{encontrados}. [{tipo.upper()}] {monto} - "
                  f"{descripcion_limpia}")
    if encontrados == 0:
        print("No se encontraron transacciones con esa descripción.")


def main():
    """Función principal del gestor de finanzas."""
    usuario = input("¿Cuál es tu nombre? ").strip().title()
    transacciones = []
    opcion = ""

    while opcion != OPCION_SALIR:
        print(f"\n=== GESTOR DE FINANZAS DE {usuario.upper()} ===")
        print(f"{OPCION_INGRESO}. Registrar un ingreso")
        print(f"{OPCION_GASTO}. Registrar un gasto")
        print(f"{OPCION_BALANCE}. Ver balance actual")
        print(f"{OPCION_HISTORIAL}. Ver historial")
        print(f"{OPCION_BUSCAR}. Buscar por descripción")
        print(f"{OPCION_SALIR}. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == OPCION_INGRESO:
            monto = pedir_monto_valido("¿Cuánto dinero ganaste? $")
            desc = pedir_texto_valido("Ingresa una descripción: ")
            registrar_transaccion(transacciones, monto, "ingreso", desc)
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance = ingresos - gastos
            print(f"Ingreso registrado. Balance: {ver_balance(balance)}")

        elif opcion == OPCION_GASTO:
            monto = pedir_monto_valido("¿Cuánto dinero gastaste? $")
            desc = pedir_texto_valido("Ingresa una descripción: ")
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance_actual = ingresos - gastos

            if monto > balance_actual:
                print("¡Advertencia! El gasto supera tu saldo.")

            registrar_transaccion(transacciones, monto, "gasto", desc)
            balance = balance_actual - monto
            print(f"Gasto registrado. Balance: {ver_balance(balance)}")

        elif opcion == OPCION_BALANCE:
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance = ingresos - gastos
            print(f"\nTu saldo actual es: {ver_balance(balance)}")

        elif opcion == OPCION_HISTORIAL:
            mostrar_historial(transacciones, "ingreso")
            mostrar_historial(transacciones, "gasto")

        elif opcion == OPCION_BUSCAR:
            palabra = pedir_texto_valido("Ingresa la palabra a buscar: ")
            buscar_transacciones(transacciones, palabra)

        elif opcion == OPCION_SALIR:
            print(f"\n¡Hasta luego, {usuario}!")

        else:
            print("Opción no válida. Elige un número del 1 al 6.")


if __name__ == "__main__":
    main()