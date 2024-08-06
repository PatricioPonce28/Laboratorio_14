# Importación de librerías
import os  
from stdiomask import getpass
from prettytable import PrettyTable

# Definición de variables globales y constantes
calificacionesTupla = ()
calificacionesLista = list(calificacionesTupla)
numCalifi = 0

# Definición de funciones 
# Función para menú de opciones 
def menu():
    print("--------------- SISTEMA SAEW 2.0 -------------")
    print("\n\t\t- Módulo profesor -\n")
    print("-------------------Bienvenido ----------------\n")
    print("¿Qué acción desea realizar?: ")
    print('*  1) Ingresar calificaciones')
    print('*  2) Mostrar calificaciones de menor a mayor')
    print('*  3) Mostrar calificaciones de mayor a menor')
    print('*  4) Detalle de las calificaciones')
    print('*  5) Mostrar detalle de las calificaciones por archivo')
    print('*  6) Salir del sistema')
    tipoAccion = int(input("Ingrese la opción: "))
    while tipoAccion not in [1, 2, 3, 4, 5, 6]:
        print("Opción Incorrecta: prueba de nuevo: ")
        tipoAccion = int(input("Ingrese la opción: "))
    return tipoAccion

def agregarCalificaciones(arreglo, n):
    for i in range(n):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación final del estudiante {i + 1} (0-20): "))
                if 0 <= calificacion <= 20:
                    arreglo.append(calificacion)
                    break
                else:
                    print("La calificación debe estar en el rango de 0 a 20.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

# Función para mostrar calificaciones 
def mostrarCalificaciones(arreglo):
    arreglo.sort()
    print("Las calificaciones registradas de menor a mayor son:")
    print(arreglo)

def mostrarCalificacionesDesc(arreglo):
    arreglo.sort(reverse=True)
    print("Las calificaciones registradas de mayor a menor son:")
    print(arreglo)

# Función para guardar información 
def guardarArchivo(data):
    archivo = open("BDD/reporte.txt", 'w')
    archivo.write('* Detalle de las calificaciones\n')
    archivo.write(f'{data}')
    archivo.close()
    print("Información almacenada exitosamente")

# Función para mostrar información 
def mostrarArchivo():
    archivo = open("BDD/reporte.txt")
    lineas = archivo.readlines()
    for l in lineas:
        print(l, end="")
    archivo.close()

# Función para mostrar detalles de calificaciones 
def mostrarDetalle(arreglo, califi):
    contadorApro = 0
    contadorRecha = 0
    contadorSuspen = 0
    sumCalifi = 0
    for i in arreglo:
        sumCalifi += i

    for i in calificacionesLista:
        if 1 <= i <= 8:
            contadorRecha += 1
        if 9 <= i <= 13:
            contadorSuspen += 1
        if 14 <= i <= 20:
            contadorApro += 1

    promedio = round((sumCalifi / califi), 2)

    # Crear una instancia de PrettyTable
    tabla = PrettyTable()
    # Definir los encabezados de la tabla
    tabla.field_names = ["Total estudiantes", "Promedio", "Aprobados", "Suspensos", "Reprobados"]
    # Agregar filas de datos a la tabla
    tabla.add_row([califi, promedio, contadorApro, contadorSuspen, contadorRecha])
    print(tabla)
    guardarArchivo(tabla)

# Función principal main 
def main():
    password = getpass(prompt="Ingresa tu contraseña: ", mask='*')
    if password == "sistemas":
        clear_command = 'clear' if os.name == 'posix' else 'cls'
        os.system(clear_command)
        global numCalifi  # Declarar la variable como global
        caso = menu()
        while caso != 6:
            if caso == 1:
                os.system(clear_command)
                numCalifi = int(input("Ingrese el número de estudiantes del curso: "))
                agregarCalificaciones(calificacionesLista, numCalifi)
                os.system(clear_command)
                caso = menu()
            elif caso == 2:
                os.system(clear_command)
                mostrarCalificaciones(calificacionesLista)
                caso = menu()
            elif caso == 3:
                os.system(clear_command)
                mostrarCalificacionesDesc(calificacionesLista)
                caso = menu()
            elif caso == 4:
                os.system(clear_command)
                mostrarDetalle(calificacionesLista, numCalifi)
                caso = menu()
            elif caso == 5:
                os.system(clear_command)
                mostrarArchivo()
                print()
                caso = menu()
        os.system(clear_command)
        print("Muchas gracias")
    else:
        print("Usuario no encontrado")

# Ejecutar la función main
main()
