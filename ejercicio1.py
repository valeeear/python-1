import os
os.system('cls')
var_totalGFlt = 0
cons_libretaInt = 5000
cons_borradorInt = 1000
cons_reglaInt = 1000
cons_lapizInt = 1500
cons_morralInt = 300000
cons_coloresInt = 60000
cons_uniformesInt = 200000

var_nombreStr = input('Nombre estudiante ->')
var_contactoStr = input('Contacto estudiante ->')
var_direccionStr = input('Direccion estudiante ->')
var_presupuestoFlt = float(input('Presupuesto ->'))
var_controlBln = True
while var_controlBln == True: 
    os.system('cls')
    print('CLIENTE:' , var_nombreStr)
    var_opcionStr = int(input('<<<MENÚ DE OPCIONES>>>\n\n1. LIBRETA\n2. BORRADOR\n3. REGLA\n4. LAPIZ\n5. MORRAL\n6. COLORES\n7. UNIFORMES\n8. SALIR\n->'))
    if var_opcionStr >= 1 and var_opcionStr <= 7:
        var_cantidadInt = int(input('Cantidad ->'))
    if var_opcionStr == 1:
            var_totalGFlt += (var_cantidadInt * cons_libretaInt)
    if var_opcionStr == 2:
            var_totalGFlt += (var_cantidadInt * cons_borradorInt)
    if var_opcionStr == 3:
            var_totalGFlt += (var_cantidadInt * cons_reglaInt)   
    if var_opcionStr == 4:
            var_totalGFlt += (var_cantidadInt * cons_lapizInt) 
    if var_opcionStr == 5:
            var_totalGFlt += (var_cantidadInt * cons_morralInt)
    if var_opcionStr == 6:
            var_totalGFlt += (var_cantidadInt * cons_coloresInt)
    if var_opcionStr  == 7:
            var_totalGFlt += (var_cantidadInt * cons_uniformesInt)
    if var_opcionStr == 8:
        print('El total a pagar es $', var_totalGFlt)   
        if var_presupuestoFlt >= var_totalGFlt:
         print('Gracias por tu compra')
        else:
            print('No tienes suficiente saldo')
        var_coltrolBln = False
    