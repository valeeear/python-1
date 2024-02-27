import os
os.system('cls')
participante1Str = input('Nombre participante 1 ->')
numeroP1Int = int(input('Numero del participante 1 ->'))
participante2Str = input('Nombre participante 2 ->')
numeroP2Int = int(input('Numero del participante 2 ->'))
var_acumuladoP1Int = 0
var_acumuladoP2Int = 0
controlInt = True
while controlInt == True:
    os.system('cls')
    print('<<<<<MENÚ DE OPCIONES>>>>>\n\n')
    print('1' ,participante1Str, 'No. ' , numeroP1Int,' ', var_acumuladoP1Int, 'km\n2.' , participante2Str, 'No. ' , numeroP2Int,' ', var_acumuladoP2Int, 'km\n3. Finalizar' )
    opcionInt = int(input('\nSeleccione una opcion ->'))
    if opcionInt >=1 and opcionInt <=2:
        var_recorridoEtapaInt = int(input('Ingrese los km recorridos ->'))
        if opcionInt == 1:
            var_acumuladoP1Int += var_recorridoEtapaInt
        if opcionInt == 2:
            var_acumuladoP2Int += var_recorridoEtapaInt
    if opcionInt == 3:
        print('Participante No.1' , participante1Str, 'Recorrido:', var_acumuladoP1Int, 'km')
        print('Participante No.2' , participante2Str, 'Recorrido:', var_acumuladoP2Int, 'km')
        enter = input('\n<ENTER> para continuar')
        controlInt = False
        