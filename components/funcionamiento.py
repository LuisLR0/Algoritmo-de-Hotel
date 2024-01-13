import os
from components import menuv2

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')







class Clientes:

    def __init__(self, fullname, edad, cedula, instancia):
        self.fullname = fullname
        self.edad = edad
        self.cedula = cedula
        self.instancia = instancia


    def monstar_info(self):
        return {
            'status': False,
            'Nombre': self.fullname,
            'Edad': self.edad,
            'Cedula': 'V ' + str(self.cedula),
            'Instancia': str(self.instancia) + ' Dias'
        }





def ruleta_clases(valor, indice):

    
    while True:
        if valor == '1':
            indice = max(0, indice - 1)
        elif valor == '2':
            indice = min(2, indice + 1)
        return indice











def mostrar_clases(idx, validar, **habitaciones):
    while True:
        os.system('clear')
        menuv2.monstar_info(validar)

        menuv2.clases(idx)
        menuv2.menu_mostrar_clase()
        valor = input('~~> ')
        idx = ruleta_clases(valor, idx)
        key = 'no_rentados' if 'no_rentados' in habitaciones else 'rentados'

        if valor == '0':
            break
        elif valor == '3' and validar == '1':
            habitaciones_clases(idx, validar, habitaciones, key)

    return idx



def modificar_eliminar_habitaciones(idx, validar, **habitaciones):
    while True:
        clear_console()
        
        menuv2.monstrar_rentadas(idx)

        print("\n")

        if len(habitaciones['rentados'][idx]) == 0:
            menuv2.habitaciones_no_rentadas()
        else:
            for hab in habitaciones['rentados'][idx]:
                print("|~~| Habitacion " + hab)

        print("\n\n")

        menuv2.menu_mostrar_clase()

        valor = input('~~> ')
        idx = ruleta_clases(valor, idx)

        if valor == '0':
            break
        elif valor == '3' and habitaciones['rentados'][idx] != {}:
            clear_console()
            habitaciones_clases(idx, validar, habitaciones, 'rentados')

    return idx




def monstrar_habitaciones_rentadas(idx, lista_habitaciones_rentadas):
    while True:
        clear_console()
        
        menuv2.monstrar_rentadas(idx)

        print("\n")

        if len(lista_habitaciones_rentadas[idx]) == 0:
            menuv2.habitaciones_no_rentadas()
        else:
            for hab in lista_habitaciones_rentadas[idx]:
                print(f'''
|~~~~~~~~| Habitacion {hab} |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        Nombre = {lista_habitaciones_rentadas[idx][hab]['Nombre']}
        Edad = {lista_habitaciones_rentadas[idx][hab]['Edad']}
        Cedula = {lista_habitaciones_rentadas[idx][hab]['Cedula']}
        Limite de Instancia = {lista_habitaciones_rentadas[idx][hab]['Instancia']}
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
''')

        print("\n\n")

        menuv2.menu_mostrar_ver()

        valor = input('~~> ')
        idx = ruleta_clases(valor, idx)

        if valor == '0':
            break

    return idx










def validacion_datos(texto_validacion, validar, tipo_validacion):
    validacion = ''
    while True:
        menuv2.monstar_info(validar)
        validacion = input(texto_validacion)
        if tipo_validacion == 'numero':
            if validacion.isdigit():
                break
            else:
                clear_console()
                print("| ~~~ Por favor, ingrese solo números. ~~~ |")
        elif tipo_validacion == 'string':
            if all(palabra.isalpha() for palabra in validacion.split()):
                break
            else:
                clear_console()
                print("| ~~~ Por favor, ingrese solo letras. ~~~|")
        else:
            print("Tipo de validación no reconocido.")
    clear_console()
    return validacion











def ingresar_datos_habitaciones(validar):
    clear_console()
    comprobar = False

    name = validacion_datos('|~~| Ingresa tu Nombre Completo: ', validar, 'string')
    edad = validacion_datos('|~~| Ingresa tu Edad: ', validar, 'numero')
    cedula = validacion_datos('|~~| Ingresa tu Cedula: C.I ', validar, 'numero')
    
    while True:
        clear_console()
        menuv2.monstrar_instancia()
        if comprobar:
            print('| ~~ Ingrear bien los datos, Minimo 31 dias de instancia ~~ |\n')
        instancia = input('|~~| Ingresa Los Dias de Instancia: ')
        try:
            instancia = int(instancia)
            if 1 <= instancia <= 31:
                comprobar = False
                break
            else:
                comprobar = True
        except ValueError:
            comprobar = True

    cliente_info = Clientes(name, edad, cedula, instancia).monstar_info()

    return cliente_info











def rentar_habitacion(validar, idx, val, habitaciones):
    cliente_info = ingresar_datos_habitaciones(validar)

    habitaciones['no_rentados'][idx][val].update(cliente_info)
    habitaciones['rentados'][idx][val] = habitaciones['no_rentados'][idx].pop(val, None)






def modificar_habitacion(validar, idx, val, habitaciones):
    while True:

        clear_console()

        print(f'''
|~~~~~~~~| Habitacion {val} |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        Nombre = {habitaciones['rentados'][idx][val]['Nombre']}
        Edad = {habitaciones['rentados'][idx][val]['Edad']}
        Cedula = {habitaciones['rentados'][idx][val]['Cedula']}
        Limite de Instancia = {habitaciones['rentados'][idx][val]['Instancia']}
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
''')
        menuv2.menu_modificar_eliminar()

        valor = input('~~> ')

        if valor == '0':
            break
        elif valor == '1':
            cliente_info = ingresar_datos_habitaciones(validar)
            habitaciones['rentados'][idx][val].update(cliente_info)
        elif valor == '2':
            habitaciones['no_rentados'][idx][val] = habitaciones['rentados'][idx].pop(val, None)
            break











def habitaciones_clases(idx, validar, habitaciones, key):
    comprobar = False
    while True:
        clear_console()
        menuv2.monstar_info(validar)

        # Ordenar las habitaciones antes de imprimirlas
        for hab in sorted(habitaciones[key][idx], key=lambda x: int(x.split('-')[1])):
            print('|~~| Habitacion ' + hab) 

        print('\n')
        if comprobar:
            print('| ~~ Habitacion Invalida ~~ |\n')

        val = input('|~~| Ingrese la habitacion: ').upper()

        if val in habitaciones[key][idx] and key == 'no_rentados':
            rentar_habitacion(validar, idx, val, habitaciones)
        elif val in habitaciones[key][idx] and key == 'rentados':
            modificar_habitacion(validar, idx, val, habitaciones)
        else:
            comprobar = True
            if val == '0':
                break











def crear_habitaciones(cantidad, lista_habitaciones): #Puedo colocar para que agrege las habitaciones que este disponible
    letras = ['A', 'B', 'C']
    for a in range(3):
        for i in range(cantidad):
            temp = f'{letras[a]}-{i+1}'
            lista_habitaciones[a][temp] = {'status': True}