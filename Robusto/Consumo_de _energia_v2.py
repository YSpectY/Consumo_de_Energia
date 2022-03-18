consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32}
 },
}

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

def total_por_region(region):

    if region not in informacion.keys():
        return 'region no existe'

    ciudades_region = informacion[region]

    total_consumo_en_region = 0
    for ciudad_region in ciudades_region:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region ==  ciudad:
                    total_consumo_en_region += sum(consumo_energia[planta][ciudad]['consumos']) * consumo_energia[planta][ciudad]['tarifa']

    return total_consumo_en_region

def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta no proveé energía a la ciudad de ' + ciudad

    total_consumo_en_planta = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo_en_planta

def total_consumo_ciudad_C(ciudad):
    if ciudad not in consumo_energia['Coca Codo Sinclair'].keys():
        return 'No hay planta de Coca Codo Sinclair en la ciudad de:' + ciudad

    total_consumo_por_ciudad = sum(consumo_energia['Coca Codo Sinclair'][ciudad]['consumos'])
    print( 'El consumo de energía de la planta Coca Codo Sinclair en la ciudad de',ciudad,'es de',total_consumo_por_ciudad,"MWh")

def total_consumo_ciudad_S(ciudad):
    if ciudad not in consumo_energia['Sopladora'].keys():
        return 'No hay planta de Sopladora en:' + ciudad

    total_consumo_por_ciudad = sum(consumo_energia['Sopladora'][ciudad]['consumos'])
    print( 'El consumo de energía de la planta Sopladora en la ciudad de',ciudad,'es de',total_consumo_por_ciudad,"MWh")

op = -1
while op != 0:
    print('--------------------------------------------------','<1> Total de energía consumida por Planta y Ciudad','<2> Total de Energia por Ciudad ','<3> Dinero Recaudado por Region ','<0> Salir', sep='\n')
    op = int(input('Ingrese una opción:'))
    if op == 1:
        print('-Total de Energía Consumida en una Ciudad y una Planta Especifica-')
        planta = input('Ingrese el nombre de la Planta: ')
        ciudad = input('Ingrese el nombre de la Ciudad: ')
        total = total_consumo_por_planta_ciudad(planta, ciudad)
        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)
    elif op == 2:
        print('-Total de Energia por Ciudad-')
        ciudad = input('Ingrese el nombre de la Ciudad: ', 'En las siguientes ciudades', 'Guayaquil', 'Quito', 'Manta', 'Loja', 'Tena', sep='\n')
        totalC = total_consumo_ciudad_C(ciudad)
        totalS = total_consumo_ciudad_S(ciudad)
        if type(totalC and totalS)==int:
            print(totalC)
            print(totalS)
        else:
            print(totalC)
            print(totalS)
    elif op == 3:
        print('-Total por Región-', 'En las siguientes regiones', 'Costa', 'Sierra', 'Oriente', sep='\n')
        region = input('Ingrese región: ')
        total = total_por_region(region)
        print(region, ':', total, '\n')