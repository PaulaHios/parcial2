from funcionparcial import* #Esta linea me importa las funciones que yo he realizado 
from datetime import datetime as dt #Y esta me permite traer funciones de librerias

#ANALISIS DEL PROBLEMA. Para el desarrollo del problema decidi divirdirlo en dos partes, la primera se encarga de captar la informacion del paciente y procesar sus datos(para analisis de resultados) y la segunda se ocupa de acomodar la informacion de los datos del paciente en un diccionario, ya que gracias a su estructura llave valor resultado facil poder hacer una busqueda
#Por medio de la implementtacion de funciones y librerias se busca disminuir los errores humanos y ademas reutilizar lineas de codigo que se pueden utilizar en varias ocasiones

dicc_paciente = {} #diciionario para almacenar pacientes
contPACIENTE = 0 #contador de pacientes 

while True: #ciclo principal para ejecutar el menú
    '''este try se usa para establecer de forma correcta el conteo de intentos cuando se pide ingresar un nuero
    sea real o imaginario, si en alguna petición se exceden los intentos, las funciones correpondientes arrojarán
    un error que será vadilado con el except correspondiente a este try'''
    try: 
        #despliegue del menu
        menu = int(valINT('''\n=========================\nMenú principal\n===========================
                              \n1)Ingresar un paciente.
                              \n2)Informede afiliación EPS.
                              \n3)Borrar paciente.
                              \n4)Salir.
                              \nIngrese el numeral que desea realizar:  '''))
        #opciones 
        if menu == 1:
            #opción 1: se ingresan los datos del paciente 
            nombre = input('\nIngrese el nombre del paciente: ')
            gen = input('\nIngrese genero del paciente: F para femenino, M para masculino: ')
            gen = gen.upper()
            edad = valINT('\nIngrese la edad del paciente: ')
            if gen == 'F':
                 ask = input("\nLa usuaria presenta menopausia? S para si o N para No: ")
                 ask = ask.upper()
                 if ask == 'S':
                      print('\nPaciente menopausica')
                 else: 
                     pass  
                 
            while True:     
              d = int(valINT('\nIngrese dia de nacimiento del paciente: '))
              m = int(valINT('\nIngrese mes de nacimiento del paciente: '))
              a = int(valINT('\nIngrese el año de nacimiento del paciente: '))
              try:
                  fecha = dt(a,m,d)
                  break
              except ValueError:
                  print('\nRectifique la fecha de ingreso')
    
            id = int(valINT('\nIngrese el documento del paciente sin puntos ni coma: ')) 
            rangolh = float(valFLOAT('\nIngrese los resultados de su examen Hormona  Luteinizante: '))
            eps = funEPS('''\nde aacuerdo a la siguiente informacion ingrese la letra correspondiente a su EPS o SI para sisben
                        \nS para Sura, C para Coomeva, M para medimas ,I para IPS Universitaria o ST para Salud Total: ''')
            cod,contPACIENTE = seriePAC(eps,contPACIENTE)
            
            if gen == 'F':
                if edad <= 18:
                    if rangolh <= 5 :
                        diag = "Hormona normal"
                    else:
                        diag = "hormona alta"
                elif ask == 'N':
                    if rangolh < 25:
                        diag = "Hormona normal"
                    else:
                        diag = "hormona alta"
                else:
                    if rangolh < 52.3:
                        diag = "Hormona normal"
                    else:
                        diag = "hormona alta"
            
            else:
                if edad <= 18:
                    if rangolh <= 1.8 :
                        diag = "Hormona normal"
                    else:
                        diag = "hormona alta"
                else:
                    if rangolh <= 8.6 :
                        diag = "Hormona normal"
                    else:
                        diag = "hormona alta"
                        
            dicc_paciente[id]=[nombre,cod,fecha,edad,(rangolh,diag)]
            print(f"\nPaciente {nombre} identificado con cédula {id} ingresado exitosamente , su resultado es {diag}")

        elif menu == 2:
            #opción 2: se usa para buscar información de la base de datos (diccionario)
            #submenu para buscar la información
            op = valINT('''\n1. Buscar paciente
                  \n2. Ver cantidad de pacientes totales
                  \n3. Ver cantidad de pacientes menores de 10
                  \n4. Ver cantidad de pacientes mayores de 60
                  \ningrese una de las opciones anteriores:''')
            if op == 1:
                #oción para buscar un paciente
                id_pac = valINT("\ningresa el documento del paciente que deseas buscar: ")
                da_pa = dicc_paciente.get(id_pac)
                if da_pa == None:
                    print(f"\n el paciente identificado con {id_pac} no se encuentra registrado")
                else:
                    print(f'''\nel paciente {da_pa[0]} con codigo de EPS {da_pa[1]} presenta el sieguiente resultado de LH {da_pa[4][0]}, por lo que se establece que su diagnostico es {da_pa[4][1]}''')
                      
            elif op == 2:
                #opción 2:para buscar determinar el total de pacientes
                print(f'\n Hay {contPACIENTE} pacientes registrados.')
                
            elif op == 3:
                #opción 3 para determinar el numero de pacientes enores de 10 años
                pac_10 = filter(lambda x: x[3] < 10, dicc_paciente.values())
                cont = len(list(pac_10))
                print(f"\nHay {cont} pacientes menores de 10 años.")
            
            elif op == 4:
                #opción 4 para determinar el numero de pacientes mayores de 60
                pac_60 = filter(lambda x: x[3] > 60, dicc_paciente.values())
                cont = len(list(pac_60))
                print(f"\nHay {cont} pacientes mayores de 60 años.")
            
            else: 
                print("\nno has ingresado una opción correcta")
                pass
                      
        elif menu == 3:
            #opcion para eliminar pacientes 
            id_pac = valINT("\ningresa el documento del paciente que deseas eliminar: ")
            da_pa = dicc_paciente.get(id_pac)
            if da_pa == None:
                print("\nel paciente ingresado no se ha registrado aún.")
            else:
                dicc_paciente.pop(id_pac)   
                print(f"\el paciente identificado con {id_pac} ha sido eliminado exitosamente")
        
        elif menu == 4:
            #opcion para salir 
            print("=========================\nSalio del programa exitosamente\n===========================")
            break     
        
        else: 
            # si no se ingresa una opción valida se vuelve al menu principal
            print("no has ingresado una opción correcta")
            pass

    except ValueError:
        print("has excedido el limite de intentos")
        pass

 
                       