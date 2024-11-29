import board
import movimiento as mv
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_tablero(tablero):
    """
    Funcion para imprimir el tablero

    Parametros
    ----------
        tablero: list[list[str]]
            Corresponde al tablero de juego

    Retorno
    -------
        None
    """

    limpiar_pantalla()

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end='')
    print()

    for i, fila in enumerate(tablero):

        print(f'{i + 1} | ', end='')

        for columna in fila:
            print(columna, end=' ')

        print(f'| {i + 1}')

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end='')
    print()


def buscar_robot(tablero):
    for i, fila in enumerate(tablero):
        for j, columna in enumerate(fila):
            if columna == board.ROBOT:
                return i, j
    return -1, -1


def mover_robot(tablero, direccion):
    fila, columna = buscar_robot(tablero)
    fila_obj, columna_obj = fila, columna

    if direccion == mv.ARRIBA:
        fila_obj -= 1 # fila = fila - 1
    elif direccion == mv.ABAJO:
        fila_obj += 1
    elif direccion == mv.IZQUIERDA:
        columna_obj -= 1
    elif direccion == mv.DERECHA:
        columna_obj += 1
    else:
        print('No se reconoce la direccion')

    if fila_obj < 0 or columna_obj < 0 or \
        fila_obj >= len(tablero) or columna_obj >= len(tablero[0]):
        print('Movimiento no valido')
        return

    if tablero[fila_obj][columna_obj] == board.SPACE:
        tablero[fila][columna] = board.OBSTA

        tablero[fila_obj][columna_obj] = board.ROBOT
    else:
        print('Movimiento no valido')

def mover_caja(tablero, direccion):
    fila, columna = buscar_robot(tablero)
    fila_obj, columna_obj = fila, columna

    if direccion == mv.ARRIBA:
        fila_obj -= 1 # fila = fila - 1
    elif direccion == mv.ABAJO:
        fila_obj += 1
    elif direccion == mv.IZQUIERDA:
        columna_obj -= 1
    elif direccion == mv.DERECHA:
        columna_obj += 1
    else:
        print('No se reconoce la direccion')

    if fila_obj < 0 or columna_obj < 0 or \
        fila_obj >= len(tablero) or columna_obj >= len(tablero[0]):
        print('Movimiento no valido')
        return

    if tablero[fila_obj][columna_obj] == board.SPACE:
        tablero[fila][columna] = board.OBSTA
        tablero[fila_obj][columna_obj] = board.ROBOT
    else:
        print('Movimiento no valido')
def win(tablero):
    victoria = True

    for fila in tablero:
        for columna in fila:
            if columna == board.SPACE:
                victoria = False

    return victoria

def leer_direccion():
    """
    Lee la dirección del usuario Numpy

    Retorno
    -------
        str: dirección en la que va a mover el robot
    """
    direccion = input('Ingrese el movimiento (W/A/S/D) o X para salir: ')
    direccion = direccion.upper()

    if direccion == 'W':
        return mv.ARRIBA
    elif direccion == 'A':
        return mv.IZQUIERDA
    elif direccion == 'S':
        return mv.ABAJO
    elif direccion == 'D':
        return mv.DERECHA
    elif direccion == 'X':
        return mv.EXIT
    else:
        return leer_direccion()


def juego():
    tab = board.leer_tablero("nivel_1") 
    
def juego():
    tab = board.leer_tablero("nivel_2") 

def juego():
    tab = board.leer_tablero("nivel_3")  

    imprimir_tablero(tab)
    direccion = leer_direccion()

    while direccion != mv.EXIT and not win(tab):
        mover_robot(tab, direccion)
        imprimir_tablero(tab)
        direccion = leer_direccion()

    print('Chao')

def manual(idioma):
    menu_manual={
        'es':{
            'desc': ' el juego consiste en algo ',
            board.ROBOT:'es el robot',
            board.OBSTA:' es un ostaculo',
        },
        'en':{
            'desc': ' el juego consiste en algo ',
            board.ROBOT:'this is a pretty robot',
            board.OBSTA:' this is an awful obtacule',
        }
    }
    for k in menu_manual[idioma]:
        if k !='desc':
            print(f'\t{k}-{menu_manual[idioma][k]}')
            
        else:
            print(menu_manual[idioma][k])

def menu():
    lang=input("indique el idioma(en/es): ")
    mi_menu={
        'es': {
            '1' :'Iniciar',
            '2' : 'ver manual del juego ',
            '3' : 'salir',
            '4' : 'selecciona nivel',
            
        },
        'en':{
            '1' : 'start new game',
            '2' : 'show manual',
            '3' : 'Exit',
            '4'  : 'select level',
            }

    }
    print("-------------------------------------")
    nivel=input("indique el nivel: ")
    menu_niveles={
        'es': {
            '1' : 'nivel_1',
            '2' : 'nivel_2',
            '3' : 'nivel_3',
        }
    }
    for k in mi_menu:
    
        print(f'{k}.{mi_menu[k]}')
    # print("1: Iniciar 🐱‍🏍")
    # print("2: Iniciar juego nuevo🐱‍👤")
    # print("3: Salir👌")}
    print("-------------------------------------")
    opt = input("ingrese la opcion de preferencia  ")
    if opt=="1":
        juego()
    elif opt =="2":
        juego()
    elif opt=="3":
        juego ()   
    elif opt=="4":
        juego ()  
    else:
        print("Opcion no valida")
        menu()

menu()

