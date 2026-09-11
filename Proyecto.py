#AVANCE 3: Módulos y Funciones Reusables
# Descripción: Este programa calcula las finanzas 
# diarias separando la lógica en funciones 
# independientes con paso de parámetros y return.


# Gestor de finanzas con saludo personalizado

def registrar_ingreso(balance, monto):
    # Recibe el balance actual y el monto ganado, calcula la suma y devuelve el nuevo balance.
    nuevo_balance = balance + monto
    return nuevo_balance

def registrar_gasto(balance, monto):
    # Recibe el balance actual y el monto gastado, calcula la resta y devuelve el nuevo balance.
    nuevo_balance = balance - monto
    return nuevo_balance

def ver_balance(balance):
    # Recibe el balance actual y simplemente lo devuelve para mostrarlo.
    return balance

# Solicitamos el nombre para personalizar la experiencia
usuario = input("¿Cuál es tu nombre? ")

# Inicializamos el balance en 0
balance = 0.0

# Solicitamos los datos al usuario mediante input y los convertimos a número decimal
mi_ingreso = float(input(f"Hola {usuario}, ¿cuánto dinero ganaste hoy? "))
mi_gasto = float(input("¿Cuánto dinero gastaste hoy? "))

# Actualizamos el balance llamando a las funciones y pasando los parámetros correspondientes
balance = registrar_ingreso(balance, mi_ingreso)
balance = registrar_gasto(balance, mi_gasto)

# Mostramos el resultado final personalizado con formato de 2 decimales
print(f"{usuario}, tu dinero actual es: ${ver_balance(balance):.2f}")