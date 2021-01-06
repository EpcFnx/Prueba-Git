def interes_progresivo():
    ahorros = int(input('Ingresar capital inicial \n'))
    medida = str(input('Elegir [mes/año]\n'))
    if medida == 'año':
        interes = 'anual'
    elif medida == 'Año':
        interes = 'anual'
    elif medida == 'Mes':
         interes = mensual
    elif medida == 'mes':
        interes = 'mensual'       
    else:
         print ('¿Eh?')
    if interes == 'mensual':
        medida_pl = 'meses'
    elif interes == 'anual':
        medida_pl = 'años'           
    tasa_interes = float(input('Ingresar la tasa de interés %s en decimales \n' % interes))
    tiempo = int(input('Ingresar cantidad de %s \n' % medida_pl))
    dash =  '=' * 85
    dash_ = '-' * 85
    print('Se muestran los valores correspondientes a cada %s' % medida)
    for x in range(0, (tiempo+1)): 
        if x == 0:
            print(dash)
            print(' {:^10s} {:>25s} {:>25s} {:>20s} ' .format(medida.upper(), 'INICIAL', 'INTERÉS', 'TOTAL'))
            print(dash)
        elif x < (tiempo + 1):
            inicial = ahorros
            interés = ahorros * tasa_interes
            ahorros = ahorros + interés
            print(' {:^10d} {:>25.3f} {:>25.3f} {:>20.3f} ' .format(x, inicial, interés, ahorros))
            print(dash_)
        else:
            interés = ahorros * tasa_interes
            ahorros = ahorros + interés
            inicial = ahorros - interés
            print(' {:^10d} {:>25.3f} {:>25.3f} {:>20.3f} ' .format(x, inicial, interés, ahorros))
            print(dash) 
