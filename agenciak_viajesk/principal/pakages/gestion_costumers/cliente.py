#imports
from pakages.gestion_UI.screenUI import pausaP, clearP
from pakages.gestion_id.identificador import idClientes

#Esta funcion crea y comprueva clientes si no existe lo introduce en lista
def crear_cliente(agencia):
    """Esta funcion gestiona la creacion y comprobacion de clientes
        y los introduce en la lista clientes en forma de dict
        con formato  cliente = {'categoria': 'C',
                                'destinos' : (idDestinos visitados),
                                'id_cliente' : 'CLM-1',
                                'nom_cliente' : 'Carlos Lucena Montes'
                                 }
        esta funcion recibe una lista agencia = [[{cliente},],[{destino},],[{reserva},]]"""
    print('\n\tEntro en opcion\n\t\t --> 2-Añadir un nuevo cliente <--')
    idCL,nomC = idClientes(agencia)
    try:
        for l in nomC:
            l.isalpha()      
    except ValueError:
        print('\n\t\tEl nombre de una persona no puede contener numeros')
        return None
    else:   
        if len(agencia[0])==0:
            agencia[0].append({'categoria': 'C',
                            'destinos' : ' ',
                            'id_cliente' : None,
                            'dir_cliente':None,
                            'nom_cliente' : None})
            print(f'Ups......INCREIBLE!!!!\n\t--->>>->>->{nomC.title()}<-<<--<<<---\n****QUE LOCURA***!Verdad?¿\n\t\t!!!!Es el primer cliente de la agencia!! GENIAL..!¡')
            pausaP()
            pass

        for cliente in agencia[0]:
            print(cliente)
            cClient =  cliente.get('nom_cliente')
            print(cClient)

        match nomC:
            case nomC if nomC == 'Salir':
                print('\n\t\tSaliendo de la opcion Crear cliente..')
                flagCl = False
                clearP()
                return None
            case nomC if nomC in cliente.values():
                print(f'\n\tEl nombre del cliente que trata de introducir--->{nomC} ya esta en el sistema como cliente\n\t\t {cliente}')
                cD = input('''\n\tVamos a comprovar su direccion:\n\tEscriva su direccion en ste formato: calle  numero de edificio  numero de piso    
                            \n\tSi se mudó en el ultimo año por favor:\n\t\t Indique su **anterior** direccion postal en el segundo intento''')
                if nomC in cliente.values() and cD not in  cliente.values():
                    clearP()    
                    try: cD2 = tuple(input('''\n\tVamos a comprovar su direccion:\n\tEscriva su direccion en ste formato:--> 
                                        \n--> nombre calle     numero de edificio    numero de piso <-- \n\t\t--->>----->>                    <<---<<--- \n\t\t\t --> DE SU ANTERIOR PISO <--'''))
                    except ValueError:
                        print('\n\tIntroduzca el nombre en el formato indicado si comas u otros separadores')  
                    clearP()
                    if nomC  in cliente.values()  and cD2 not in cliente.values():
                        print (f'\n\n\tEl cliente {nomC} esta en el sistema con su Anterior direccion por favor\n\t introduzca la NUEVA direccion ')
                        newAd = input('\n\n\tEscriba su direccion en este formato:\n\n\t--> nombre de calle   numero de edificio  numero de piso')
                        print(f'Se va a actualizar: -->{nomC} ')
                        cliente['dir_cliente'] = newAd
                        print(f'\n\tLa direccion del cliente: -->{nomC} \n\tHa sido actualizada: -->{cliente}')
                        clearP()
                        
            case nomC if nomC not in cliente.values():
                cD = input('\n\tEscriva su direccion en ste formato:--> nombre de calle,  numero de edificio,  identificador de piso')
                print(type(cD),cD) 
                if len(agencia[0]) > 1:
                    agencia[0].append({'categoria': 'C',
                                        'destinos' : ( ),
                                        'id_cliente' : idCL,
                                        'dir_cliente': cD,
                                        'nom_cliente' : nomC
                                        })
                    print(f'El cliente : {nomC} ha sido introducido con EXITO en el sistema con:...\n\t\t---> id:{idCL} direccion:{cD} ')
                    pausaP()
                    clearP()
                elif len(agencia[0]) == 1 and cClient == None:
                    agencia[0][0]= {'categoria': 'C',
                                    'destinos' : ( ),
                                    'id_cliente' : idCL,
                                    'dir_cliente': cD,
                                    'nom_cliente' : nomC
                                    }
                else:
                    agencia[0]
                print(agencia[0])
                pausaP()
                clearP()
            case _:
                print('\n\t\tEntro en else pero no tendria que haber entrado...Que mieldad NENNNG')
                
print('\t\t----<<<--->>Salio de la opcion<<--->>>----...')
                


#MUESTRA CLIENTES SI LOS HAY

def mostrar_clientes(agencia):
    """Esta funcion printa la lista de clientes
    en la base de datos de la  agencia. Esta lista 
    [{dict}, ] esta annidada en la lista agencia. 
    Y recibe la lista agencia """
    print('\n\tEntro en opcion\n\t\t --> 6-Mostrar tod@s l@s clientes <--')
    try:
        len(agencia[0]) >= 1
    except ValueError:
        print('\n\t\t-->> --> La agencia no tiene clientes en base de datos <--   <<--')
        pausaP()

    if len(agencia[0]) == 0:
        print('\n\t:--->> COMO NO existen clientes en la base de datos para Mostrar <<----:')
        try:
            iC= str(input('\n\t\tDesea crear un nuevo client@?¿\n\t\tSi <-----> No <------------')).lower()
        except ValueError:
            print('\n\t\tIndique unicamente Si o No')
        else:
            if iC == 'si':
                print('\n\tRedirigiendo a menu principal....----->>---->>>---->>>>\n------>>--<<espere mientras entro en su opcion>>--<<-----\n\t\t-->SELECCIONË::__>-->  1- para Añadir un nuev@ client@...')
                crear_cliente(agencia)
                clearP()
                return None
            else:
                print('\n\tSaliendo de la opcion Mostrar Clientes')
                clearP()
    else:
        print('\n\t\tAqui tiene la lista de clientes en base de datos:')
        
        for cliente in agencia[0]:
            for k,v in cliente.items():
                print(f'\n{k} >----< {v} ', end = '\t --><-- \n')
                pausaP()
        clearP()

    print('\t\t----<<<--->>Salio de la opcion<<--->>>----...')
    clearP()
    return None

