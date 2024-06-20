#ESTE MODULO GENERA IDENTIFICADORES A PARTIR DE UNA ENTRADA str
from pakages.gestion_UI.screenUI import pausaP, clearP 

def idDestinos(agencia):
    iDes = len(agencia[2])
    flagD = True
    while flagD:
            try: 
                lugar = input('Introduzca la ciudad de destino: o salir para terminar ').lower()
            except ValueError:
                    print('La ciudad no puede ser un numero')
            else:
                if not lugar:
                    print('El campo no puede quedar vacio ') 
                elif lugar == 'Salir':
                    print('Saliendo opcion 1-Añadir destinos--')
                    return None
                         
                lL = lugar.split(' ')
                print(type(lL),lL,len(lL))
                pausaP()
                lenL = len(lL)
                iDC = ''
                iDes += 1
                
                if lenL>1:
                    for p in lL:
                        for l in p[0]:
                            iDC += l.upper()
                    
                    iDC += '-' + str(iDes)
                elif lenL==1:
                    c = lugar[0:3]
                    print(c)
                    pausaP()
                    for l in c:
                        iDC += l.upper()
                    iDC += '-' + str(iDes)
                idYlugar = iDC, lugar
            return idYlugar
    


#Este modulo Crea identificadores de clientes

def idClientes(agencia):
    iRC = len(agencia[0])
    print(iRC)
    flagCl = True
    while flagCl:
        nomC = None
        try: 
            nomC = str(input('\n\t\tIntroduzca el nombre completo del cliente \n\tFormato nombre: carlos apellido1: fernandez apellido2: gomez \n\t o ---> salir').title())
                 
        except ValueError:
            print('\n\t\tEl nombre de una persona no puede contener numeros')
            pausaP()
            
        else:
            if not nomC:
                print('El Campo no puede quedar vacio')
                pausaP()
            elif nomC == 'Salir':
                    print('Saliendo opcion 2-Añadir destinos--')
                    return None
            else:
                nL = nomC.split(' ')
                print(type(nL),len(nL),nL)
                idCL = ' '
                for n in nL:
                    idCL += n[0]
                print(idCL)
                iRC += 1 
                idCL = idCL+'-'+str(iRC)
                print(idCL)
                idYnomC = idCL,nomC
            return idYnomC
    pausaP()