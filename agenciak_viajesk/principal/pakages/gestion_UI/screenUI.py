#Esta funciones limpian y pausan la pantalla durante el uso del programa
import os

def clearP():
    """Esta funcion limpia la pantalla 
        cuando se produce una seleccion o un retorno"""
    os.system('cls')





def pausaP():
    """Esta funcion pausa la ejecucion del programa
        para que el usuario pueda leer o decidir"""

    print('\n\t\t-->_>_>--<<Pulse --<enter>-- para seguir>>--<_<_<-- ')
    input()
