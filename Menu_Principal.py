from Temas import Temas
from Videos import Videos

Ciclo_Principal = True

while Ciclo_Principal == True:
    
    print('---MENU PRINCIPAL---')
    print('1.-Temas')
    print('2.-Videos')
    print('3.-Cursos Temas Videos')
    print('4.-Cursos Temas')
    print('5.-Cursos')
    print('6.-Empleados')
    print('7.-Salir')

    Opcion_Principal = int(input('Elija el numero de la seccion deseada: '))

    if Opcion_Principal == 1:
        
        Ciclo_Temas = True

        while Ciclo_Temas == True:

            print('---MENU TEMAS---')
            print('Acciones Disponibles:')
            print('1.-Guardar un Tema')
            print('2.-Consultar la informacion de todos los Temas')
            print('3.-Consultar la informacion de un Tema por ID')
            print('4.-Regresar al menu principal')

            Opcion_Temas = int(input('Elija el numero de la seccion deseada: '))

            if Opcion_Temas == 1:
                
                T1 = int(input('Ingrese el ID del Tema: '))
                T2 = input('Ingrese el nombre del Tema: ')
                Tema = Temas(T1, T2)
                Tema.guardar()
                print('Guardado con exito')

    elif Opcion_Principal == 2:
        pass
    elif Opcion_Principal == 3:
        pass
    elif Opcion_Principal == 4:
        pass
    elif Opcion_Principal == 5:
        pass
    elif Opcion_Principal == 6:
        pass
    elif Opcion_Principal == 7:
        pass
    else:
        print('Opcion no valida')