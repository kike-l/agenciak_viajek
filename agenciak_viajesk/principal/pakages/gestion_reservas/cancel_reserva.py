#MODULO CANCELAR RESERVA
from pakages.gestion_UI.screenUI import pausaP, clearP 
from pakages.gestion_reservas.crear_reserva import reservar

def cancelar_Reserva(agencia):
    """ Este modulo cambia la key estado reserva de 'activa a cancelada o al reves.
        Recibe la lista agencia y """
    
    print('\n\tBienvenido a opcion: ---> Cancelar Reservas')
    pausaP()
    if len(agencia[2])==0:
        print('\n\t\t-->>--:-->> NO HAY reservas en la base de datos:\n\t\t\t\t Desea crear una \n\t\t\t\t >>>>>   Si -->?¿<-- No   <<<<<  ')
        
    flagCR = True
    while flagCR:
        idR = input('\n\t\tIntroduzca el identificador numerico de la reserva que desea modificar.')
        for reserva in agencia[2]:
            confRes = reserva.get('id_reserva')
            estRes = reserva.get('estado_reserva')
            if idR == confRes:
                print(f'\n\t\tDesea modificar el estado de la reserva {reserva} ?¿\n\t\t estado actual --> {estRes}')
                conf = input('\n\t\tIntroduzca \n\t\t\tSi>----o----<No   para continuar').lower()
                clearP()
                if conf == 'si' and reserva['estado_reserva'] == 'Activa':
                    reserva['estado_reserva'] = 'Cancelada'
                    print(f'Reserva modificada correctamente {reserva}')
                elif conf == 'si' and reserva['estado_reserva'] == 'Cancelada':
                    reserva['estado_reserva'] = 'Activa'
                    print(f'Reserva modificada correctamente {reserva}')
                else:
                    print(f'Decidio no cambiar el estado de su reserva {reserva}')
                    flagCR = False
                    clearP()
                    return None
            elif confRes == None:
                print(f'\n\t\tLa reserva seleccionada {idR} no existe actualmente\n\t\tDesearia crear la reserva?¿')
                conf = input('Indique si >----< no ').lower()
                clearP()
                match conf:
                    case 'si' :
                        print('\n\tRedirigiendo a menu principal....----->>---->>>---->>>>\n------>>--<<espere mientras entro en su opcion>>--<<-----\n\t\t-->SELECCIONË::__>--> 5- para crear una reserva nueva...')
                        reservar(agencia)
                        flagCR = False
                        return None
                    case 'no' :
                        print('seleccione otra reserva..')
    clearP()
    print('\t\t----<<<--->>Salio de la opcion<<--->>>----...')

