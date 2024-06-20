#Funcion que crea y comprueva reservas-
from pakages.gestion_UI.screenUI import pausaP, clearP 
from pakages.gestion_destino.crear_destino import crear_destino
from pakages.gestion_costumers.cliente import crear_cliente


def reservar(agencia):

    print('\n\tBienvenido a opcion: ---> Realizar Reservas')
    flagR = True
    iRes = len(agencia[2])
    while flagR:
        codDest = input('\n\t\tIndique el codigo de destino:\n\t\tFormato--> MEX-12 o salir para terminar ').upper()
        if not codDest:
            ('El campo no puede quedar vacio')
            pausaP()
        lDest = []
        for destino in agencia[1]:
            confD = destino.get('id_destino')
            lDest.append(confD) 
            print(destino,confD)
            pausaP()
        if codDest not in lDest :
            print(f'\n\t\tEl destino seleccionado {codDest} no existe actualmente\n\t\tDesearia introducirlo?¿')
            conf = input('Indique si >----< no ').lower()
            match conf:
                case 'si' :
                    print('\n\tRedirigiendo a menu principal....----->>---->>>---->>>>\n------>>--<<espere mientras entro en su opcion>>--<<-----\n\t\t-->SELECCIONË::__>-->2-Añadir un nuevo destino')
                    crear_destino(agencia)
                    clearP()
                    break
                case 'no' :
                    print('seleccione otro destino..')
                    clearP()
                    break
        
        print(destino)
        match codDest:
            case codDest if codDest == 'SALIR': 
                flagR = False
                clearP()
                print('\n\t\tRedirigiendo a menu principal')
                return None
            
            case codDest if codDest in lDest:
                for destino in agencia[1]:
                    if codDest == destino['id_destino']:
                        costD = destino.get('precio_destino')
                flagC = True
                while flagC:
                    idC = input('Introduzca el identificador del cliente: o cancelar').upper()
                    if not idC:
                            print('El campo no puede quedar vacio\n\t\t\t---->>-> ejemplo identificador HYT-456')
                    match idC:
                        case idC if idC:
                            if idC == 'CANCELAR':
                                clearP()
                                print('---->>--> Cancelando <--<<----')
                                pausaP()
                                flagR = False
                                flagC= False
                                return None
                            for cliente in agencia [0]:
                                c_Cliente = cliente.get('id_cliente')
                                if c_Cliente == idC:
                                    n_client = cliente.get('nom_cliente')
                                    cliente['destinos'] += codDest 
                                    print(f'\n\tSe va a crear una reserva a nombre de--> {n_client}')
                                    pausaP() 
                                    while True:
                                        try:
                                            fecha = str(input('Introduzca la fecha de salida o salir para cancelar:\n\t\t formato:--->  16/07/2024')).lower()
                                        except ValueError:
                                            print('Introduzca la fecha en el formato indicado')
                                        else:
                                            if not fecha:
                                                print('el campo no puede quedar vacio')
                                            elif fecha == 'salir':
                                                clearP()
                                                print('---->>--> Cancelando <--<<----')
                                                pausaP()
                                                flagR = False
                                                flagC= False
                                                return None
                                            clearP()
                                            iRes += 1
                                            d = {
                                                'categoria': 'R',
                                                'id_reserva': iRes,
                                                'codigo_destino' : codDest,
                                                'id_cliente' : idC,
                                                'estado_reserva':'Activa',
                                                'Fecha_salida' : fecha,
                                                'precio_destino' : costD  }
                                            agencia[2].append(d)
                                        print(f'\n\t\tEstimado {n_client}\n Su nueva reserva id: {iRes} con destino: {codDest} Tiene prevista salida: {fecha} y un coste de: {float(costD)}--€')
                                        pausaP()
                                        d.clear()
                                        print(d)
                                        return None    
                            
                            
                            
                                                    
            case codDest if c_Cliente == None:
                
                while True:
                    clearP()
                    print(f'\n\t\tEl cliente seleccionado {idC} no existe actualmente\n\t\tDesearia introducirlo?¿')
                    pausaP()
                    conf = input('\n\tIndique:\n\t\t\t si >----< no  para cancelar la reserva ').lower()
                    if conf:
                        flagcod = True
                        while flagcod:
                            match conf:
                                case 'si' :
                                    clearP()
                                    print('\n\tRedirigiendo a menu principal....----->>---->>>---->>>>\n------>>--<<espere mientras entro en su opcioin>>--<<-----\n\t\t-->SELECCIONË::__>-->2-Añadir un nuevo cliente')
                                    flagcod = False
                                    crear_cliente(agencia)
                                    break      
                                case 'no' :
                                    clearP()
                                    print('seleccione otro cliente..')
                                    break

                    elif not conf:
                        print('\n\t\tEl campo no pude quedar vacio')
                        clearP()
    print('\n\t\tSaliendo de la opcion: ---> Crear Reserva')

