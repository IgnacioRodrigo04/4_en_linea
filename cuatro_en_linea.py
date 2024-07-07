from typing import List
VACIO = " "
PRIMER_SIMBOLO = "X"
SEGUNDO_SIMBOLO = "O"


def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
    """
    tablero = []
    for i in range (n_filas):
        fila = []
        for j in range (n_columnas):
            fila.append(" ")
        tablero.append(fila)
    return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    
    turnos_acum = 0
    for fila in tablero:
      for columna in fila:
         if columna != VACIO:
            turnos_acum += 1
    return turnos_acum % 2 == 0
    


def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """

    for fila in list(reversed(tablero)):
        if 0 <= columna <= len(tablero[0]) - 1 and fila [columna] == VACIO:
            if es_turno_de_x (tablero):
                simbolo = PRIMER_SIMBOLO
            else: 
                simbolo = SEGUNDO_SIMBOLO
            fila [columna] = simbolo
            return True
    return False


def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for columnas in tablero[0]:
        if columnas == VACIO:
            return False
    return True


        




def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`

    EJEMPLO: para el siguiente tablero, el ganador es 'X' por tener un cuatro en
    línea en diagonal
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', 'X', ' ', ' '],
            [' ', 'O, ''O', 'X', 'X', 'X', 'O'],
        ]
    """

    for fila_index, fila in enumerate(reversed (tablero)):
        for columna_index in range (len(fila)):
            simbolo = tablero [fila_index][columna_index]
            if simbolo != VACIO and es_ganador(simbolo, tablero, fila_index, columna_index):
                return simbolo
            
    return VACIO





def es_ganador(simbolo, tablero, fila_index, columna_index) -> bool:
    return verificar_derecha(tablero, fila_index, columna_index, simbolo) or verificar_arriba(tablero, fila_index, columna_index, simbolo) or verificar_arriba_derecha(tablero, fila_index, columna_index, simbolo) or verificar_arriba_izquierda(tablero, fila_index, columna_index, simbolo)


def verificar_derecha(tablero, fila_index, columna_index, simbolo):
    return len(tablero[fila_index]) - columna_index >= 4 and  tablero[fila_index][columna_index + 1] == simbolo and tablero[fila_index][columna_index + 2] == simbolo and tablero[fila_index][columna_index + 3] == simbolo

def verificar_arriba(tablero, fila_index, columna_index, simbolo):
    return len(tablero) - fila_index >= 4 and  tablero[fila_index + 1][columna_index] == simbolo and tablero[fila_index + 2][columna_index] == simbolo and tablero[fila_index + 3][columna_index] == simbolo

def verificar_arriba_derecha(tablero, fila_index, columna_index, simbolo):
    return len(tablero[fila_index]) - columna_index >= 4 and len(tablero) - fila_index >= 4 and tablero[fila_index + 1][columna_index + 1] == simbolo and tablero[fila_index + 2][columna_index + 2] == simbolo and tablero[fila_index + 3][columna_index + 3] == simbolo

def verificar_arriba_izquierda(tablero, fila_index, columna_index, simbolo):
    return len(tablero[fila_index]) - columna_index <= 4 and len(tablero) - fila_index >= 4 and tablero[fila_index + 1][columna_index - 1] == simbolo and tablero[fila_index + 2][columna_index - 2] == simbolo and tablero[fila_index + 3][columna_index - 3] == simbolo




