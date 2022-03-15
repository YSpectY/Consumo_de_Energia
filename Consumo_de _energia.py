# 1. Solicite al usuario el nombre de una planta y de una ciudad
# y presente el total de megavatios de consumos para dicha ciudad en dicha planta.
# 2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves son los nombres de las plantas generadoras 
# y el total megavatios que cada planta le ha dado a ciudad. 
# Si la planta no entrega energía a la ciudad entonces esa planta no debería aparecer en el nuevo diccionario
# 3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la región Sierra.


consumo_energia = {
 'Coca Codo Sinclair': {
 'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
 'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
 },
 'Sopladora': {
 'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
 'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
 'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}
energia_ciudad = {
    'Quito': {
        'Coca Codo Sinclair':{'Megavatios producidos':(4753)},
        'Sopladora':{'Megavatios producidos': (5676)}},
    'Guayaquil': {
        'Coca Codo Sinclair':{'Megavatios producidos':(920)},
        'Sopladora':{'Megavatios producidos':(3404)}},
    'Loja': {
        'Sopladora':{'Megavatios producidos': (456)}},
}
total_ccs_quito= 4753 * 65
total_ccs_guayaquil = 920 * 84
total_sopladora_quito = 5676 * 79
total_sopladora_guayaquil = 3404 * 55
total_sopladora_loja = 456 * 32
consumo_coca_quito=consumo_energia['Coca Codo Sinclair']['Quito']['consumos']
consumo_coca_guayaquil=consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']
consumo_sopladora_quito=consumo_energia['Sopladora']['Quito']['consumos']
consumo_sopladora_guayaquil=consumo_energia['Sopladora']['Guayaquil']['consumos']
consumo_sopladora_loja=consumo_energia['Sopladora']['Loja']['consumos']
ciudades_ccs = ciudades_sopladora = 1
energia_quito_ccs=energia_ciudad['Quito']['Coca Codo Sinclair']['Megavatios producidos']
energia_quito_sopladora=energia_ciudad['Quito']['Sopladora']['Megavatios producidos']
energia_guayaquil_ccs=energia_ciudad['Guayaquil']['Coca Codo Sinclair']['Megavatios producidos']
energia_guayaquil_sopladora=energia_ciudad['Guayaquil']['Sopladora']['Megavatios producidos']
energia_loja_sopladora=energia_ciudad['Loja']['Sopladora']['Megavatios producidos']

def consumo_ccs ():
    print('Consumo total de la planta en',ciudades_ccs, 'es de: ' ,consumo , 'MW')
    print('........................................','',sep='\n')

def consumo_sopladora ():
    print('Consumo total de la planta en',ciudades_sopladora, 'es de: ' ,consumo , 'MW')
    print('........................................','',sep='\n')

def err_mayus ():
    print('Error','Escriba la ciudad con la primera letra en mayuscula','.................................', sep='\n')

consumo = 0
por = 0
while por != 'Salir':
    planta = ciudad = region = 0
    print('Por que metodo va a realizar','Planta','Ciudad','Region', sep='\n')
    por = input('Escriba la opcion que desea revisar o escriba Salir para terminar el programa: ')
    if por == 'Planta':
        while planta != 'Salir':
            print('Plantas:','Coca Codo Sinclair','Sopladora', sep='\n')
            planta = input('Escriba el nombre de la planta que desee revisar o Salir para para regresar: ')
            if planta == 'Coca Codo Sinclair':
                ciudades_ccs = 0
                while ciudades_ccs != 'Salir':
                    consumo = 0
                    print('Ciudades:','Guayaquil','Quito', sep='\n')
                    ciudades_ccs = input('Escriba el nombre de la ciudad que desee a revisar o Salir para regresar: ')
                    if ciudades_ccs == 'Guayaquil':
                        for i in consumo_coca_guayaquil:
                            consumo += i
                        consumo_ccs()
                        break
                    elif ciudades_ccs == 'Quito':
                        for i in consumo_coca_quito:
                            consumo += i
                        consumo_ccs()
                        break
                    elif ciudades_ccs == 'Salir':
                        break
                    else:
                        err_mayus()
            elif planta == 'Sopladora':
                ciudades_sopladora = 0
                while ciudades_sopladora != 'Salir':
                    consumo = 0
                    print('Ciudades:','Guayaquil','Quito','Loja', sep='\n')
                    ciudades_sopladora = input('Escriba el nombre de la ciudad que desee a revisar o Salir para regresar: ')
                    if ciudades_sopladora == 'Guayaquil':
                        for i in consumo_sopladora_guayaquil:
                            consumo += i
                        consumo_sopladora()
                        break
                    elif ciudades_sopladora == 'Quito':
                        for i in consumo_sopladora_quito:
                            consumo += i
                        consumo_sopladora()
                        break
                    elif ciudades_sopladora == 'Loja':
                        for i in consumo_sopladora_loja:
                            consumo += i
                        consumo_sopladora()
                        break
                    elif ciudades_sopladora == 'Salir':
                        break
                    else:
                        err_mayus()
            elif planta == 'Salir':
                break
            else:
                err_mayus()
    elif por == 'Ciudad':
        while ciudad != 'Salir':
            print('Ciudades:','Guayaquil','Quito','Loja', sep='\n')
            ciudad = input('Escriba el nombre de la ciudad que desee a revisar o Salir para regresar: ')
            if ciudad == 'Guayaquil':
                print('Megavatios producidos por la planta Coca Codo Sinclair en Guayaquil:',energia_guayaquil_ccs)
                print('Megavatios producidos por la planta Sopladora en Guayaquil:',energia_guayaquil_sopladora)
                break
            elif ciudad == 'Quito':
                print('Megavatios producidos por la planta Coca Codo Sinclair en Quito:',energia_quito_ccs)
                print('Megavatios producidos por la planta Sopladora en Quito:',energia_quito_sopladora)
                break
            elif ciudad == 'Loja':
                print('Megavatios producidos por la planta Sopladora en Loja:',energia_loja_sopladora)
                break
            elif ciudad == 'Salir': 
                break
            else:
                err_mayus()
    elif por == 'Region':
        while region != 'Salir':
            print('regiones:','Costa','Sierra','Oriente', sep='\n')
            region = input('Escriba el nombre de la region que desee a revisar o Salir para regresar: ')
            if region == 'Costa':
                print('El total recaudado en la costa es de:', total_sopladora_guayaquil+total_ccs_guayaquil)
            elif region == 'Sierra':
                print ('El total recaudado en la costa es de:', total_sopladora_quito+total_ccs_quito+total_sopladora_loja)
            elif region == 'Oriente':
                print('No existen datos para el oriente')
                break
            elif region == 'Salir':
                break
            else:
                err_mayus()
    elif por == 'Salir':
        break
    else:
        err_mayus()