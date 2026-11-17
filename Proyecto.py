"""Gestor de finanzas personales - Versión completa con Avance 8."""

OPCION_INGRESO = "1"
OPCION_GASTO = "2"
OPCION_BALANCE = "3"
OPCION_HISTORIAL = "4"
OPCION_ESTADISTICAS = "5"
OPCION_CALCULADORA = "6"
OPCION_BUSCAR = "7"
OPCION_SALIR = "8"


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
            desc = matriz[i][2].capitalize()
            print(f"{contador}. {monto_str} - {desc}")
    if contador == 0:
        print(f"No hay {tipo_buscado}s registrados.")


def calcular_estadisticas(matriz, tipo_buscado):
    """Calcula suma, promedio, máximo y mínimo usando índices."""
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
        print(f"\nNo hay datos para estadísticas de {tipo_buscado}s.")
        return

    promedio = total / contador

    print(f"\n--- ESTADÍSTICAS DE {tipo_buscado.upper()}S ---")
    print(f"Total acumulado: ${total:.2f}")
    print(f"Promedio por registro: ${promedio:.2f}")
    print(f"Mayor {tipo_buscado}: ${maximo:.2f}")
    print(f"Menor {tipo_buscado}: ${minimo:.2f}")


def buscar_transacciones(matriz, palabra_clave):
    """Busca y muestra transacciones que contienen la palabra clave."""
    palabra = palabra_clave.strip().lower()
    print(f"\n--- RESULTADOS DE BÚSQUEDA: '{palabra_clave}' ---")
    encontrados = 0
    for i in range(len(matriz)):
        desc = matriz[i][2].lower()
        if palabra in desc:
            encontrados += 1
            tipo = matriz[i][1]
            monto = f"${matriz[i][0]:.2f}"
            descripcion_limpia = matriz[i][2].capitalize()
            print(f"{encontrados}. [{tipo.upper()}] {monto} - "
                  f"{descripcion_limpia}")
    if encontrados == 0:
        print("No se encontraron transacciones con esa descripción.")


def calculadora_auxiliar():
    """Permite realizar cálculos rápidos sin afectar las finanzas."""
    print("\n--- CALCULADORA FINANCIERA AUXILIAR ---")
    print("1. Operaciones básicas (+, -, *, /)")
    print("2. Calcular porcentaje")

    sub_opcion = input("Elige una opción de cálculo (1-2): ")

    if sub_opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: No se puede dividir entre cero.")
                return
        else:
            print("Operador no válido.")
            return

        print(f"Resultado del cálculo: {resultado:.2f}")

    elif sub_opcion == "2":
        cantidad = float(input("Ingresa la cantidad base: "))
        porcentaje = float(
            input("Ingresa el porcentaje a calcular (ej. 15): ")
        )
        resultado = (cantidad * porcentaje) / 100
        print(f"El {porcentaje}% de {cantidad:.2f} es: {resultado:.2f}")
    else:
        print("Opción de cálculo no válida.")


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
        print(f"{OPCION_ESTADISTICAS}. Ver estadísticas")
        print(f"{OPCION_CALCULADORA}. Usar calculadora auxiliar")
        print(f"{OPCION_BUSCAR}. Buscar por descripción")
        print(f"{OPCION_SALIR}. Salir")

        opcion = input("Selecciona una opción (1-8): ")

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

        elif opcion == OPCION_ESTADISTICAS:
            calcular_estadisticas(transacciones, "ingreso")
            calcular_estadisticas(transacciones, "gasto")

        elif opcion == OPCION_CALCULADORA:
            calculadora_auxiliar()

        elif opcion == OPCION_BUSCAR:
            palabra = pedir_texto_valido("Ingresa la palabra a buscar: ")
            buscar_transacciones(transacciones, palabra)

        elif opcion == OPCION_SALIR:
            print(f"\n¡Hasta luego, {usuario}!")

        else:
            print("Opción no válida. Elige un número del 1 al 8.")


if __name__ == "__main__":
    main()