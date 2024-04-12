#funciones para usar en el archivo implementación.py

#función para validar valores enteros y numero de intentos
def valINT(msj):
    N = 0
    while N < 3:
        try: 
            entrada = int(input(msj))
            return entrada
        except:
            print('Ingrese solo numeros enteros, por favor.')
            N+=1
            
    raise ValueError("Se excedió el número de intentos de ingreso de números enteros")

#función para validar valores flotantes y numero de intentos
def valFLOAT(msj):
    N = 0
    while N < 3:
        try: 
            entrada = float(input(msj))
            return entrada
        except:
            print('Ingrese solo numeros reales, por favor.')
            N+=1
    raise ValueError("Se excedió el número de intentos de ingreso de números flotantes")

#función para validar la eps del paciente actual
def funEPS(msj):
    while True:
        entrada = input(msj)   
        entrada = entrada.upper()
        if entrada == 'S' or entrada =='C' or entrada =='I' or entrada == 'ST' or entrada == 'M' or entrada == 'SI':
            return entrada
        else:
            print("\npor favor, ingresa una EPS valida.")
            pass
    
#función para crear el codigo de usuario
def seriePAC(SS,contador):
    contador = contador+1
    if SS == 'S':
        return f'EPS-SURA_{contador}', contador
    elif SS == 'C':
        return f'EPS-COOMEVA-{contador}', contador
    elif SS == 'I':
        return f'EPS-IPS U_{contador}', contador
    elif SS == 'ST':
        return f'EPS-SALUDTOTAL_{contador}', contador
    elif SS == 'M':
        return f'EPS-MEDIMAS_{contador}', contador
    elif SS == 'SI':
        return f'EPS-SISBEN_{contador}', contador
    
    
    



