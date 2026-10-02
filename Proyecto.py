# Descripción: Gestor de finanzas interactivo que permite realizar 
# múltiples operaciones mediante un menú continuo y valida los datos de entrada.

# --- FUNCIONES ---

def registrar_ingreso(balance, monto):
    """Calcula la suma del balance actual y el monto ganado."""
    nuevo_balance = balance + monto
    return nuevo_balance


def registrar_gasto(balance, monto):
    """Calcula la resta del balance actual y el monto gastado."""
    nuevo_balance = balance - monto
    return nuevo_balance


def ver_balance(balance):
    """Devuelve el monto formateado como texto con 2 decimales y signo $."""
    return f"${balance:.2f}"


def pedir_monto_valido(mensaje):
    """Asegura mediante un ciclo while que el usuario ingrese un monto positivo."""
    monto = float(input(mensaje))
    while monto <= 0:
        print(" Error: El monto debe ser un número mayor a 0.")
        monto = float(input(mensaje))
    return monto


# --- PROGRAMA PRINCIPAL ---

# Solicitamos el nombre para personalizar la experiencia
usuario = input("¿Cuál es tu nombre? ")

# Inicializamos el balance y los contadores
balance = 0.0
cant_ingresos = 0
cant_gastos = 0
total_ingresado = 0.0
total_gastado = 0.0

opcion = ""

# Ciclo principal: se repite hasta que el usuario elija la opción "5"
while opcion != "5":
    print(f"\n=== GESTOR DE FINANZAS DE {usuario.upper()} ===")
    print("1. Registrar un ingreso")
    print("2. Registrar un gasto")
    print("3. Ver balance actual")
    print("4. Ver resumen del día")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        monto = pedir_monto_valido("¿Cuánto dinero ganaste? $")
        balance = registrar_ingreso(balance, monto)
        
        # Actualizamos contadores y acumuladores
        cant_ingresos += 1
        total_ingresado += monto
        print(f" Ingreso registrado correctamente. Balance actual: {ver_balance(balance)}")

    elif opcion == "2":
        monto = pedir_monto_valido("¿Cuánto dinero gastaste? $")
        
        # Alerta opcional si el gasto supera el balance disponible
        if monto > balance:
            print(" ¡Advertencia! Este gasto supera tu saldo disponible. Tu balance quedará negativo.")
            
        balance = registrar_gasto(balance, monto)
        
        # Actualizamos contadores y acumuladores
        cant_gastos += 1
        total_gastado += monto
        print(f" Gasto registrado correctamente. Balance actual: {ver_balance(balance)}")

    elif opcion == "3":
        print(f"\n Tu saldo actual es: {ver_balance(balance)}")

    elif opcion == "4":
        print("\n--- RESUMEN DE LA SESIÓN ---")
        print(f"Número de ingresos: {cant_ingresos} (Total: ${total_ingresado:.2f})")
        print(f"Número de gastos:   {cant_gastos} (Total: ${total_gastado:.2f})")
        print(f"Saldo final:        {ver_balance(balance)}")

    elif opcion == "5":
        print(f"\n¡Hasta luego, {usuario}! Gracias por usar el gestor de finanzas.")

    else:
        print(" Opción no válida. Por favor, elige un número del 1 al 5.")