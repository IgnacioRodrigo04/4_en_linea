import cuatro_en_linea as juego

VACIO = " "
PRIMER_SIMBOLO = "X"
SEGUNDO_SIMBOLO = "O"
MINIMO_FILA = 4
MAXIMO_FILA = 10
MINIMO_COLUMNA = 4  
MAXIMO_COLUMNA = 10


#solicita al usuario el tamaño del tablero de juego y devuelve las dimensiones
def pedir_tablero(): 
   n_filas = input("Ingrese el largo del juego: ")
   n_columnas = input("Ingrese el ancho del juego: ")
   return n_filas, n_columnas

#validamos las dimensiones del tablero
def validar_tablero(n_filas, n_columnas):

   if n_filas.isdigit() and n_columnas.isdigit:
      n_filas = int(n_filas)
      n_columnas = int(n_columnas)

      if not MINIMO_FILA <= n_filas <= MAXIMO_FILA:
         print("El largo del tablero no puede ser menor que 3 ni mayor que 10 ")
      if not MINIMO_COLUMNA <= n_columnas <= MAXIMO_COLUMNA:
         print("El ancho del tablero no puede ser menor que 3 ni mayor que 10 ")
      if MINIMO_FILA <= n_filas <= MAXIMO_FILA and MINIMO_COLUMNA <= n_columnas <= MAXIMO_COLUMNA:
         return True
      
   else:
      print("La entrada solo acepta numeros ")

   return False

#imprimimos el tablero
def imprimir_tablero(tablero):
   for i in range (len(tablero[0])):
      print(f"| {i + 1} ", end="")
   print("|")
   for i in range (len(tablero[0])):
      print("----", end="")
   print("-")
   for fila in tablero:
      for columna in fila:
         print(f"| {columna} ", end="")
      print("|")

#crea el tablero de juego pedido por el usuario y validado
def tablero():
   tablero_valido = False
   n_filas= 0
   n_columnas = 0
   while not tablero_valido:
      n_filas, n_columnas = pedir_tablero()
      tablero_valido = validar_tablero(n_filas, n_columnas)
   tablero = juego.crear_tablero(int(n_filas), int(n_columnas))
   return tablero



#pregunta al usuario hasta que ponga una columna valida, para jugar.
def imprimir_turno(tablero):
   n_columnas = len(tablero[0])
   if juego.es_turno_de_x(tablero):
      print(f"Es turno de X ")
   else:
      print("Es turno de O ")
   columna_valida = False
   while not columna_valida:
      columna_elegida = input(f"Eliga una columna entre 1 y {n_columnas}: ")
      if columna_elegida.isdigit() and 0 < int(columna_elegida) <= n_columnas:
         juego.insertar_simbolo(tablero, int(columna_elegida) - 1)
         columna_valida = True
      else:
         print("Entrada Invalida ")
   imprimir_tablero(tablero)

#imprime los turnos hasta que termine el juego
def realizar_jugada(tablero):
   while not juego.tablero_completo(tablero) and juego.obtener_ganador(tablero) == VACIO:
      imprimir_turno(tablero)

def mostrar_resultado(tablero):
   hay_ganador = juego.obtener_ganador(tablero)
   if hay_ganador == PRIMER_SIMBOLO :
      print("GANO X ")
   elif  hay_ganador == SEGUNDO_SIMBOLO:
      print ("GANO O ")
   else:
      print("¡EMPATE! ")
   


def main ():
   tablero_vacio = tablero()
   imprimir_tablero(tablero_vacio)
   realizar_jugada(tablero_vacio)
   mostrar_resultado(tablero_vacio)
main()


