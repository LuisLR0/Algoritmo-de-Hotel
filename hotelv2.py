from components import menuv2
from components import funcionamiento
import os

indice = 0

clientes_on = []

habitaciones = [{}, {}, {}]
habitaciones_rentadas = [{}, {}, {}]

funcionamiento.crear_habitaciones(10, habitaciones)


while True:
    os.system('clear')
    menuv2.mostrar_menu()
    for i in clientes_on:
        print(i.monstar_info())
    
    validar = input('|~~| Ingresar Opcion: ')

    if validar == '1':
        indice = funcionamiento.mostrar_clases(indice, validar, no_rentados=habitaciones, rentados=habitaciones_rentadas)
    elif validar == '2':
        indice = funcionamiento.monstrar_habitaciones_rentadas(indice, habitaciones_rentadas)
    elif validar == '3':
        indice = funcionamiento.modificar_eliminar_habitaciones(indice, validar, no_rentados=habitaciones, rentados=habitaciones_rentadas)

    elif validar == '0':
        break
