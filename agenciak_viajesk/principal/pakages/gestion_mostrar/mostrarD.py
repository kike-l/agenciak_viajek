# Aqui se incorpora funcion mostrar
from pakages.gestion_UI.screenUI import pausaP, clearP 
from pakages.gestion_destino.crear_destino import crear_destino


def mostrar_destinos(agencia):
    """Esta funcion retorna la lista de destinos
    en venta por la agencia. Esta lista [{dict}, ] 
    esta annidada en la lista agencia. Y recibe la 
    lista agencia """
    print('\n\tEntro en opcion\n\t\t\t -->>>->--> 5-Mostrar Destinos <--<-<<<--')
    pausaP()


    if len(agencia[1]) == 0:
        print('\n\n\t\t-->> La tienda no tiene destinos en stock <<--\n\n')
        pausaP()
        clearP()
        try:
            iD= str(input('\n\n\t\tDesea crear un nuevo destino?¿\n\n\n\t\t\t\t--->->>>->  Si <-----> No  <-<<<-<---\n')).lower()
            iD == 'si' or iD == 'no'
        except ValueError:
            print('\n\t\tIndique unicamente:\n\t\t\t\t--->->>>->   Si <-----> No   <-<<<-<---\n')
        else:
            if iD == 'si':
                print('\n\t\tRedirigiendo a menu principal....----->>---->>>---->>>>\n\t>>>>>>>>>------>>--<<espere mientras entro en su opcion>>--<<-----\n\t\t-->SELECCIONË::--->>>-->  1-Añadir un nuevo destino\n')  
                crear_destino(agencia)
            else:
                print('\n\t\t--->>-->> Saliendo de la opcion Mostrar Destinos <<--<<---')
                clearP()
                return None
    else:
        print('\n\t\t-->> Aqui tiene la lista de destinos en stock:--->>>-->>->\n\n')
        for destino in agencia[1]:
            for k,v in destino.items():
                print(f'\t**{k}** >---::---<( {v}', end = '  )--><--@  \n')   

        