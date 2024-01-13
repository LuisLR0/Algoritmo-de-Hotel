def mostrar_menu():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║            RENTAR HABITACIONES DE UN HOTEL               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║       1-.) Rentar Una Habitacion                         ║
║                                                          ║
║       2-.) Habitaciones Rentadas                         ║
║                                                          ║
║       3-.) Modificar/Eliminar                            ║
║                                                          ║
║       0-.) SALIR                                         ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)


def clases(clase):
    if clase == 2:
        print("""
    ╔══════════════════════════════════════════════╗
    ║       Habitaciónes Clase C - Estándar        ║
    ╠═══════════════╦══════════════════════════════╣
    ║    Tamaño     ║             20 m²            ║
    ║   Capacidad   ║          2 personas          ║
    ╠═══════════════╬══════════════════════════════╣
    ║               ║   - 1 cuarto                 ║
    ║    Cuartos    ║   - 1 baño                   ║
    ║               ║   - Cocina                   ║
    ╠═══════════════╬══════════════════════════════╣
    ║     Vistas    ║ vistas a la ciudad           ║
    ╠═══════════════╩══════════════════════════════╣
    ║          Servicios e Instalaciones           ║
    ╠══════════════════════════════════════════════╣
    ║ - Baño privado                               ║
    ║ - TV de pantalla plana                       ║
    ║ - Wi-Fi gratuito                             ║
    ║ - Aire acondicionado                         ║
    ║ - Servicio diario de limpieza                ║
    ╚══════════════════════════════════════════════╝
        """)
    elif clase == 1:
        print("""
    ╔══════════════════════════════════════════════╗
    ║        Habitaciónes Clase B - Superior       ║
    ╠═══════════════╦══════════════════════════════╣
    ║    Tamaño     ║             30 m²            ║
    ║   Capacidad   ║          3 personas          ║
    ╠═══════════════╬══════════════════════════════╣
    ║               ║   - 2 cuarto                 ║
    ║               ║   - 1 baño                   ║
    ║    Cuartos    ║   - Cocina                   ║
    ║               ║   - Sala Amplia              ║
    ║               ║   - Mini Terraza             ║
    ╠═══════════════╬══════════════════════════════╣
    ║     Vistas    ║ vistas al jardín o al mar    ║
    ╠═══════════════╩══════════════════════════════╣
    ║          Servicios e Instalaciones           ║
    ╠══════════════════════════════════════════════╣
    ║ - Baño privado con ducha                     ║
    ║ - TV de pantalla plana con canales premium   ║
    ║ - Wi-Fi gratuito                             ║
    ║ - Aire acondicionado                         ║
    ║ - Servicio diario de limpieza                ║
    ║ - Cocina equipada                            ║
    ║ - Minibar                                    ║
    ╚══════════════════════════════════════════════╝
""")
    else:
        print("""
    ╔══════════════════════════════════════════════╗
    ║       Habitaciónes Clase A - Suite Deluxe    ║
    ╠═══════════════╦══════════════════════════════╣
    ║    Tamaño     ║             50 m²            ║
    ║   Capacidad   ║          5 personas          ║
    ╠═══════════════╬══════════════════════════════╣
    ║               ║   - 4 cuartos                ║
    ║               ║   - 2 baños                  ║
    ║    Cuartos    ║   - Sala                     ║
    ║               ║   - Cocina                   ║
    ║               ║   - Terraza                  ║
    ╠═══════════════╬══════════════════════════════╣
    ║     Vistas    ║ vistas panorámica al mar     ║
    ╠═══════════════╩══════════════════════════════╣
    ║          Servicios e Instalaciones           ║
    ╠══════════════════════════════════════════════╣
    ║ - Baño privado con jacuzzi                   ║
    ║ - Sala de estar separada                     ║
    ║ - TV de pantalla plana con canales premium   ║
    ║ - Minibar gratuito                           ║
    ║ - Wi-Fi gratuito                             ║
    ║ - Aire acondicionado                         ║
    ║ - Servicio de habitaciones 24h               ║
    ║ - Desayuno incluido                          ║
    ║ - Acceso exclusivo al lounge del hotel       ║
    ║ - Caja fuerte                                ║
    ╚══════════════════════════════════════════════╝
""")
        

def menu_mostrar_clase():
    print('|~~| 1 -) ATRAS  || 2 -) SIGUIENTE || 3 -) SELECCIONAR || 0-) SALIR |~~|')

def menu_mostrar_ver():
    print('|~~| 1 -) ATRAS  || 2 -) SIGUIENTE || 0-) SALIR |~~|')

def menu_modificar_eliminar():
    print('|~~| 1 -) MODIFICAR  || 2 -) ELIMINAR || 0-) SALIR |~~|')


    
def monstar_info(seleccion):
    if seleccion == '1':
        print('''
        ╔═══════════════════════════════════════╗
        ║           RENTAR HABITACION           ║
        ╚═══════════════════════════════════════╝
    ''')
    elif seleccion == '3':
        print('''
  ╔══════════════════════════════════════════════════╗
  ║            ESCOGE CLASE DE HABITACION            ║
  ║       PARA MODIFICAR HABITACIONES RENTADAS       ║
  ╚══════════════════════════════════════════════════╝
    ''')
        


def monstrar_instancia():
    print('''
    ╔═══════════════════════════════════════╗
    ║           TIEMPO DE RESERVA           ║
    ║            LIMITE 31 DIAS             ║
    ╚═══════════════════════════════════════╝
''')


def monstrar_rentadas(seleccion):
    if seleccion == 2:
        print('''
   ╔═══════════════════════════════════════╗
   ║         HABITACIONES RENTADAS         ║
   ║                Clase C                ║
   ╚═══════════════════════════════════════╝
''')
    elif seleccion == 1:
        print('''
   ╔═══════════════════════════════════════╗
   ║         HABITACIONES RENTADAS         ║
   ║                Clase B                ║
   ╚═══════════════════════════════════════╝
''')
    else:
        print('''
   ╔═══════════════════════════════════════╗
   ║         HABITACIONES RENTADAS         ║
   ║                Clase A                ║
   ╚═══════════════════════════════════════╝
''')
        
def habitaciones_no_rentadas():
    print('''
   ╔═══════════════════════════════════════╗
   ║          NO HAY HABITACIONES          ║
   ║               RENTADAS                ║
   ╚═══════════════════════════════════════╝
''')
