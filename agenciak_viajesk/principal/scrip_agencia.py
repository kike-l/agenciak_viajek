#imports
from pakages.gestion_UI.screenUI import clearP , pausaP 
from pakages.gestion_costumers.cliente import crear_cliente, mostrar_clientes
from pakages.gestion_destino.crear_destino import crear_destino
from pakages.gestion_mostrar.mostrarC import mostrar_clientes
from pakages.gestion_mostrar.mostrarR import mostrar_reservas
from pakages.gestion_mostrar.mostrarD import mostrar_destinos 
from pakages.gestion_reservas.crear_reserva import reservar
from pakages.gestion_reservas.cancel_reserva import cancelar_Reserva





#Funcion menu
def principal(agencia):

    print('\n\tBienvenido  a nuestra agencia de viajes:\n\t Por favor haga una seleccion del menu:')
    flagMen = True
    while flagMen:
        print(""" \n\t Menu:\n
                \t\t1-Añadir un nuevo destino
                \t\t2-Añadir un nuevo cliente
                \t\t3-Realizar una reserva
                \t\t4-Cancelar una reserva
                \t\t5-Mostrar todos los destinos
                \t\t6-Mostrar todos los clientes
                \t\t7-Mostrar todas las reservas
                \t\t8-Salir""")
        pausaP()
        try:
            sel = int(input('Introduzca una seleccion del menu:'))
        except ValueError:
            clearP()
            print('\nPor favor haga la seleccion de forma numerica\n\t\t Tipo---> 1 (para seleccionar Añadir un nuevo destino) ')
        else:
            if 8 >= sel >= 1: 
                match sel:
                    case 1:
                        clearP()
                        print('\n\t\tSelecciono Añadir un nuevo destino')
                        crear_destino(agencia)
                        
                    case 2:
                        clearP()
                        print('\n\t\tSelecciono Añadir un nuevo cliente ')
                        crear_cliente(agencia)
                        
                    case 3:
                        clearP()
                        print('\n\t\tSelecciono Realizar una reserva ')
                        reservar(agencia)
                    case 4:
                        clearP()
                        print('\n\t\tSelecciono Cancelar una reserva ')
                        cancelar_Reserva(agencia)
                    case 5:
                        clearP()
                        print('\n\t\tSelecciono  Mostrar todos los destinos ')
                        mostrar_destinos(agencia)
                        
                    case 6:
                        clearP()
                        print('\n\t\tSelecciono  Mostrar todos los clientes ')
                        mostrar_clientes(agencia)
                        
                    case 7:
                        clearP()
                        print('\n\t\tSelecciono  Mostrar todos los reservas ')
                        mostrar_reservas(agencia)
                        
                    case 8:
                        clearP()
                        print('\n\t\tSelecciono  Salir del Programa ')
                        flagMen = False
                    case _:
                        clearP()
                        print('\n\t\tAlgo salio muy mal saliendo del Programa...')
                        break
            else:
                clearP()
                print('\n\t\tLa seleccion debe estar en el menu es decir entre el 1 y el 8')
      
    print('\n\t\tSalio del programa my litle Agency..Regrese pronto...y buen viaje..')

if __name__=='__main__':
    agencia = [[],[],[]]
    principal(agencia)
