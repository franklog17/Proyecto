# Proyecto Gestor de finanzas

Contexto

Este programa tiene como función llevar un control propio de las finanzas, como un cuaderno con un menu sencillo de opciones.
Funciona con 4 opciones sencillas iniciales:

1) Registrar gastos: Escribes cuánto gastaste y en qué.
2) Registrar ingresos: Cuánto dinero ganaste o recibiste.
3) Ver balance: El programa suma todo lo que ganaste-recibiste, resta todo lo que gastaste y te dice cuánto te queda automaticamente.
4) Salir.

Tengo planeado evolucionar el programa como agregar detalle de cada gasto, alertar si hay gasto excesivo o funciones mas especificas para cada opción.

#Este código solo incluye condicionales y operadores aritméticos, considerando lo visto en clase, por eso todavía no incluye menú de opciones.

def registrar_ingreso(balance, monto):
    nuevo_balance = balance + monto
    return nuevo_balance

def registrar_gasto(balance, monto):
    nuevo_balance = balance - monto
    return nuevo_balance

def ver_balance(balance):
    return balance

balance = 0
mi_ingreso = float(input("¿Cuanto dinero ganaste hoy?"))
mi_gasto = float(input("¿Cuanto dinero gastaste hoy?"))

balance = registrar_ingreso(balance, mi_ingreso)
balance = registrar_gasto(balance, mi_gasto)
print("Tu dinero actual es: ${:.2f}".format(ver_balance(balance)))
