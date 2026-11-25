"""Gestor de finanzas personales multi-usuario - Avance 9."""

OPCION_INGRESO = "1"
OPCION_GASTO = "2"
OPCION_BALANCE = "3"
OPCION_HISTORIAL = "4"
OPCION_ESTADISTICAS = "5"
OPCION_CALCULADORA = "6"
OPCION_BUSCAR = "7"
OPCION_CAMBIAR_USUARIO = "8"
OPCION_SALIR = "9"

ARCHIVO_USUARIOS = "usuarios.txt"
PALABRAS_CANCELAR = ("cancelar", "c")


def normalizar_nombre_archivo(usuario):
    """Genera un nombre de archivo seguro a partir del nombre del usuario."""
    limpio = "_".join(usuario.strip().lower().split())
    return f"transacciones_{limpio}.txt"


def cargar_usuarios(nombre_archivo):
    """Carga la lista de usuarios registrados desde un archivo."""
    usuarios = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre != "" and nombre not in usuarios:
                    usuarios.append(nombre)
    except FileNotFoundError:
        pass
    return usuarios


def guardar_usuarios(usuarios, nombre_archivo):
    """Guarda la lista de usuarios registrados en un archivo."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for usuario in usuarios:
            archivo.write(f"{usuario}\n")


def pedir_monto_valido(mensaje, permitir_cancelar=True):
    """Asegura que el monto sea mayor a cero o permite cancelar."""
    while True:
        print(mensaje)
        if permitir_cancelar:
            print("(Escribe 'cancelar' para regresar al menú)")
        entrada = input("> ").strip()

        if permitir_cancelar and entrada.lower() in PALABRAS_CANCELAR:
            return None

        try:
            monto = float(entrada)
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue

        if monto <= 0:
            print("Error: El monto debe ser mayor a 0.")
        else:
            return monto


def pedir_texto_valido(
    mensaje, permitir_cancelar=True, mostrar_ayuda_cancelar=True
):
    """Asegura que el texto no esté vacío o permite cancelar."""
    while True:
        print(mensaje)
        if permitir_cancelar and mostrar_ayuda_cancelar:
            print("(Escribe 'cancelar' para regresar al menú)")
        texto = input("> ").strip()

        if permitir_cancelar and texto.lower() in PALABRAS_CANCELAR:
            return None

        if texto == "":
            print("Error: El texto no puede estar vacío.")
        else:
            return texto


def seleccionar_o_registrar_usuario(usuarios, permitir_cancelar=True):
    """Permite elegir un usuario, registrar uno nuevo o cancelar/salir."""
    while True:
        print("\n=== REGISTRO Y SELECCIÓN DE USUARIOS ===")
        if len(usuarios) > 0:
            print("Usuarios registrados:")
            for i in range(len(usuarios)):
                print(f"{i + 1}. {usuarios[i]}")

            op_nuevo = len(usuarios) + 1
            print(f"{op_nuevo}. Registrar nuevo usuario")

            if permitir_cancelar:
                op_cancelar = len(usuarios) + 2
                print(f"{op_cancelar}. Cancelar / Salir")
            else:
                op_cancelar = None

            eleccion = input("Selecciona una opción: ").strip()

            if eleccion.isdigit():
                opcion_num = int(eleccion)
                if 1 <= opcion_num <= len(usuarios):
                    return usuarios[opcion_num - 1]
                if opcion_num == op_nuevo:
                    print("\n--- REGISTRAR NUEVO USUARIO ---")
                    nuevo_raw = pedir_texto_valido(
                        "Ingresa el nombre del nuevo usuario:",
                        permitir_cancelar=True,
                    )
                    if nuevo_raw is None:
                        print("Registro cancelado.")
                        continue
                    nuevo = nuevo_raw.title()
                    if nuevo in usuarios:
                        print("Ese usuario ya existe. Seleccionado.")
                        return nuevo
                    usuarios.append(nuevo)
                    guardar_usuarios(usuarios, ARCHIVO_USUARIOS)
                    return nuevo
                if op_cancelar is not None and opcion_num == op_cancelar:
                    return None

            print("Selección no válida. Intenta de nuevo.")
        else:
            print("No hay usuarios registrados todavía.")
            print("1. Registrar nuevo usuario")
            print("2. Salir")
            eleccion = input("Selecciona una opción (1-2): ").strip()

            if eleccion == "1":
                print("\n--- REGISTRAR USUARIO ---")
                nuevo_raw = pedir_texto_valido(
                    "Ingresa tu nombre para registrarte:",
                    permitir_cancelar=True,
                )
                if nuevo_raw is None:
                    print("Registro cancelado.")
                    continue
                nuevo = nuevo_raw.title()
                usuarios.append(nuevo)
                guardar_usuarios(usuarios, ARCHIVO_USUARIOS)
                return nuevo
            if eleccion == "2":
                return None

            print("Selección no válida. Intenta de nuevo.")


def cargar_transacciones(nombre_archivo):
    """Carga transacciones desde un archivo de texto y devuelve una matriz."""
    matriz = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia != "":
                    partes = linea_limpia.split("|")
                    if len(partes) == 3:
                        monto = float(partes[0])
                        tipo = partes[1]
                        descripcion = partes[2]
                        matriz.append([monto, tipo, descripcion])
    except FileNotFoundError:
        pass
    return matriz


def guardar_transacciones(matriz, nombre_archivo):
    """Guarda la matriz de transacciones en un archivo de texto."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for fila in matriz:
            linea = f"{fila[0]}|{fila[1]}|{fila[2]}\n"
            archivo.write(linea)


def registrar_transaccion(matriz, monto, tipo, descripcion):
    """Agrega un sub-arreglo con monto, tipo y descripción a la matriz."""
    matriz.append([monto, tipo, descripcion])


def ver_balance(balance):
    """Devuelve el monto formateado como texto con 2 decimales."""
    return f"${balance:.2f}"


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
    minimo = float("inf")

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
            print(
                f"{encontrados}. [{tipo.upper()}] {monto} - "
                f"{descripcion_limpia}"
            )
    if encontrados == 0:
        print("No se encontraron transacciones con esa descripción.")


def calculadora_auxiliar():
    """Permite realizar cálculos rápidos sin afectar las finanzas."""
    print("\n--- CALCULADORA FINANCIERA AUXILIAR ---")
    print("1. Operaciones básicas (+, -, *, /)")
    print("2. Calcular porcentaje")
    print("3. Cancelar")

    sub_opcion = input("Elige una opción de cálculo (1-3): ").strip()

    if sub_opcion == "1":
        num1 = pedir_monto_valido(
            "Ingresa el primer número:",
            permitir_cancelar=True,
        )
        if num1 is None:
            print("Cálculo cancelado.")
            return

        operador = pedir_texto_valido(
            "Ingresa la operación (+, -, *, /):",
            permitir_cancelar=True,
        )
        if operador is None:
            print("Cálculo cancelado.")
            return

        print("Ingresa el segundo número:")
        print("(Escribe 'cancelar' para regresar al menú)")
        num2_raw = input("> ").strip()
        if num2_raw.lower() in PALABRAS_CANCELAR:
            print("Cálculo cancelado.")
            return
        try:
            num2 = float(num2_raw)
        except ValueError:
            print("Error: Número no válido. Cálculo cancelado.")
            return

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
        cantidad = pedir_monto_valido(
            "Ingresa la cantidad base:",
            permitir_cancelar=True,
        )
        if cantidad is None:
            print("Cálculo cancelado.")
            return

        print("Ingresa el porcentaje a calcular (ej. 15):")
        print("(Escribe 'cancelar' para regresar al menú)")
        porcentaje_raw = input("> ").strip()
        if porcentaje_raw.lower() in PALABRAS_CANCELAR:
            print("Cálculo cancelado.")
            return
        try:
            porcentaje = float(porcentaje_raw)
        except ValueError:
            print("Error: Porcentaje no válido. Cálculo cancelado.")
            return

        resultado = (cantidad * porcentaje) / 100
        print(f"El {porcentaje}% de {cantidad:.2f} es: {resultado:.2f}")

    elif sub_opcion == "3":
        print("Cálculo cancelado.")
    else:
        print("Opción de cálculo no válida.")


def main():
    """Función principal del gestor de finanzas."""
    usuarios = cargar_usuarios(ARCHIVO_USUARIOS)
    usuario = seleccionar_o_registrar_usuario(usuarios, permitir_cancelar=True)

    if usuario is None:
        print("\nOperación cancelada. ¡Hasta luego!")
        return

    archivo_actual = normalizar_nombre_archivo(usuario)
    transacciones = cargar_transacciones(archivo_actual)
    print(f"\n¡Bienvenido/a, {usuario}!")
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
        print(f"{OPCION_CAMBIAR_USUARIO}. Cambiar o registrar usuario")
        print(f"{OPCION_SALIR}. Salir")

        opcion = input("Selecciona una opción (1-9): ").strip()

        if opcion == OPCION_INGRESO:
            print("\n--- REGISTRAR INGRESO ---")
            monto = pedir_monto_valido(
                "¿Cuánto dinero ganaste? $",
                permitir_cancelar=True,
            )
            if monto is None:
                print("Registro de ingreso cancelado.")
                continue

            desc = pedir_texto_valido(
                "Ingresa una descripción:",
                permitir_cancelar=True,
                mostrar_ayuda_cancelar=False,
            )
            if desc is None:
                print("Registro de ingreso cancelado.")
                continue

            registrar_transaccion(transacciones, monto, "ingreso", desc)
            guardar_transacciones(transacciones, archivo_actual)
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance = ingresos - gastos
            print(f"Ingreso registrado. Balance: {ver_balance(balance)}")

        elif opcion == OPCION_GASTO:
            print("\n--- REGISTRAR GASTO ---")
            monto = pedir_monto_valido(
                "¿Cuánto dinero gastaste? $",
                permitir_cancelar=True,
            )
            if monto is None:
                print("Registro de gasto cancelado.")
                continue

            desc = pedir_texto_valido(
                "Ingresa una descripción:",
                permitir_cancelar=True,
                mostrar_ayuda_cancelar=False,
            )
            if desc is None:
                print("Registro de gasto cancelado.")
                continue

            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance_actual = ingresos - gastos

            if monto > balance_actual:
                print("¡Advertencia! El gasto supera tu saldo.")

            registrar_transaccion(transacciones, monto, "gasto", desc)
            guardar_transacciones(transacciones, archivo_actual)
            balance = balance_actual - monto
            print(f"Gasto registrado. Balance: {ver_balance(balance)}")

        elif opcion == OPCION_BALANCE:
            print("\n--- BALANCE ACTUAL ---")
            ingresos = calcular_total_por_tipo(transacciones, "ingreso")
            gastos = calcular_total_por_tipo(transacciones, "gasto")
            balance = ingresos - gastos
            print(f"Tu saldo actual es: {ver_balance(balance)}")

        elif opcion == OPCION_HISTORIAL:
            mostrar_historial(transacciones, "ingreso")
            mostrar_historial(transacciones, "gasto")

        elif opcion == OPCION_ESTADISTICAS:
            calcular_estadisticas(transacciones, "ingreso")
            calcular_estadisticas(transacciones, "gasto")

        elif opcion == OPCION_CALCULADORA:
            calculadora_auxiliar()

        elif opcion == OPCION_BUSCAR:
            print("\n--- BUSCAR POR DESCRIPCIÓN ---")
            palabra = pedir_texto_valido(
                "Ingresa la palabra a buscar:",
                permitir_cancelar=True,
            )
            if palabra is None:
                print("Búsqueda cancelada.")
                continue
            buscar_transacciones(transacciones, palabra)

        elif opcion == OPCION_CAMBIAR_USUARIO:
            guardar_transacciones(transacciones, archivo_actual)
            nuevo_usuario = seleccionar_o_registrar_usuario(
                usuarios, permitir_cancelar=True
            )
            if nuevo_usuario is not None:
                usuario = nuevo_usuario
                archivo_actual = normalizar_nombre_archivo(usuario)
                transacciones = cargar_transacciones(archivo_actual)
                print(f"\n¡Bienvenido/a, {usuario}!")
            else:
                print(
                    f"\nCambio cancelado. Sigues en la sesión de {usuario}."
                )

        elif opcion == OPCION_SALIR:
            guardar_transacciones(transacciones, archivo_actual)
            guardar_usuarios(usuarios, ARCHIVO_USUARIOS)
            print(f"\n¡Hasta luego, {usuario}!")

        else:
            print("Opción no válida. Elige un número del 1 al 9.")


if __name__ == "__main__":
    main()