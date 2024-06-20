from pakages.gestion_UI.screenUI import pausaP, clearP
from pakages.gestion_id.identificador import idDestinos

#Modulo que crea y comprueva destinos
def crear_destino(agencia):
        """ Esta funcion permite crear y comprovar destinos y los acumula en la lista agencia
            en forma de diccionario cuyo formato es-->
                        ---> destino = {'categoria': 'D',
                                        'id_destino':'HAW-1',
                                        'nom_destino':'hawai',
                                        'tipo_destino':""" 'muy bonito y tal' """,
                                        'precio_destino' : 100 }
            esta funcion recibe la lista agencia """

        print('\n\tEntro en opcion\n\t\t --->>-->  1-Añadir un nuevo destino\n <--<<---')
        pausaP()
        flagD = True
        while flagD:
                try:
                    iDC, lugar = idDestinos(agencia)
                except ValueError:
                       print('\n\t\t---> La ciudad no puede ser un numero <---')
                else:
                    if lugar == 'Salir':
                        print('\n\t\t--->>--->>>--> Salindo de opcion añadir destinos <--<<<---<<--- ')
                        flagD = False
                        return None
                    elif not lugar:
                          print('\n\t\t El campo no puede quedar vacio ')
                    else:
                        flagD = False
                flagP = True      
                while flagP:
                        try:
                            precio = float(input('\n\t\tIntroduzca el precio del viaje\n'))
                        except ValueError:
                            print('\n\t\tEl precio debe ser un numero\n')                          
                        else:
                            print(type(precio))
                            if not precio:
                                print('\n\t\t El campo no puede quedar vacio\n')
                                clearP()
                            for destino in agencia[1]:
                                h = destino.get('nom_destino')
                                p = destino.get('precio_destino')
                                if lugar == h  and precio == p:
                                    print(f'\n\t\t-->-->> El destino--> {lugar} que intenta introducir ya existe !! <<--<--')
                                    flagD = False
                                    return None 
                                else:
                                    print('------Mal----')
                                    flagP = False
                                    break
                        flagD1 = True
                        while flagD1:
                            try:
                                desc = str(input('-->-->>>-> Introduzca una pequeña descripcion del destino <-<<<--<--'))        
                            except ValueError:
                                    print('\n\t\t\t -->>>--> La descripcion no deben ser solo numeros <--<<<--')
                            else:
                                flagP = False
                                flagD1 = False
                         
                        agencia[1].append({'categoria': 'D',
                                            'id_destino':iDC,
                                            'nom_destino':lugar,
                                            'tipo_destino': desc,
                                            'precio_destino' : precio })
                        print(f'\n\t\t\tDestino introducido con EXITO\n\t{iDC} {lugar} {desc} {precio}\n')
                        

        print('\t\t\t\t----<<<--->>Salio de la opcion<<--->>>----...')
        pausaP()
        clearP()
        


   
                    
                    
                        
                
