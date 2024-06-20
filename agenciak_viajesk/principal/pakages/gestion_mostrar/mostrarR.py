#Funcion que muestra reservas
from pakages.gestion_UI.screenUI import pausaP, clearP 
from pakages.gestion_reservas.crear_reserva import reservar
def mostrar_reservas(agencia):
    """Esta funcion printa la lista de reservas
    en la base de datos de la  agencia. Esta lista 
    [{dict}, ] esta anidada en la lista agencia. 
    La funcion recibe la lista agencia """

    print('\n\tEntro en opcion\n\t\t --> 7- Mostrar todas las reservas <--')
    pausaP()

    if not agencia[2]:
        print('\n\t\t-->>-->> La agencia no tiene reservas en base de datos <<--<<--')
        pausaP()
        try:
            iR= str(input('\n\t\tDesea crear una reserva?¿\n\n\t--->>--->>>--> Si <-----> No <--<<<---<<---')).lower()
        except ValueError:
            print('\n\t\tIndique unicamente Si o No')
        else:
            if iR == 'si':
                print('\n\tRedirigiendo a menu principal....----->>---->>>---->>>>\n------>>--<<espere mientras entro en su opcion>>--<<-----\n\t\t-->SELECCIONË::__>--> 3-Realizar una reserva...')
                print('\n\tSaliendo de la opcion Mostrar Reservas')
                reservar(agencia)
                clearP()
                return None
            elif iR == 'no':
                print('\n\tSaliendo de la opcion Mostrar Reservas')
                clearP()
                return None
   
    else:
        print('\n\t\tAqui tiene la lista de Reservas en base de datos:')
        for reserva in agencia[2]:
            for k,v in reserva.items():
                print(f'\n\t{k} >----< {v}', end = '\n\t\t\t---><---')
                pausaP()
        clearP()
    
    print('\t\t...----<<<--->>Salio de la opcion<<--->>>----...')
    return None
    