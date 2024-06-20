#ESte modulo muestra los clientes
from pakages.gestion_UI.screenUI import pausaP, clearP 
from pakages.gestion_costumers.cliente import crear_cliente

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