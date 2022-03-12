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
consumo_coca_quito=consumo_energia['Coca Codo Sinclair']['Quito']['consumos']
consumo_coca_guayaquil=consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']
consumo_sopladora_quito=consumo_energia['Sopladora']['Quito']['consumos']
consumo_sopladora_guayaquil=consumo_energia['Sopladora']['Guayaqil']['consumos']
consumo_sopladora_loja=consumo_energia['Sopladora']['Loja']['consumos']
menu = 1 ; ciudades_ccs = 1 ; ciudades_sopladora = 1
def consumo_ccs ():
    print('Consumo total de la planta en',ciudades_ccs, 'es de: ' ,consumo , 'MW')
    print('........................................','',sep='\n')

def consumo_sopladora ():
    print('Consumo total de la planta en',ciudades_sopladora, 'es de: ' ,consumo , 'MW')
    print('........................................','',sep='\n')

while menu != 'Salir':
    print('Plantas:','Coca Codo Sinclair','Sopladora', sep='\n')
    menu = input('Escriba el nombre de la planta que desee revisar o Salir para terminar el programa: ')
    if menu == 'Coca Codo Sinclair':
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
            else:
                print('Error','Escriba la ciudad con la primera letra en mayuscula','.................................', sep='\n')
    elif menu == 'Sopladora':
        while ciudades_sopladora != 'Salir':
            consumo = 0
            print('Ciudades:','Guayaquil','Quito','Loja', sep='\n')
            ciudades_sopladora = input('Escriba el nombre de la ciudad que desee a revisar o Salir para regresar: ')
            if ciudades_sopladora == 'Guayaquil':
                for i in consumo_sopladora_guayaquil:
                    consumo += i
                consumo_sopladora()
                break
            elif ciudades_ccs == 'Quito':
                for i in consumo_sopladora_quito:
                    consumo += i
                consumo_sopladora()
                break
            elif ciudades_ccs == 'Loja':
                for i in consumo_sopladora_loja:
                    consumo += i
                consumo_sopladora()
                break
            else:
                print('Error','Escriba la ciudad con la primera letra en mayuscula','.................................', sep='\n')