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

    #---MENU PARA LA SECCION DE TEMAS---

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

            elif Opcion_Temas == 2:
                
                print('Desplegando todos los Temas. Ejemplo: ID | NOMBRE DEL TEMA')
                Tema = Temas()
                Tema.consultar_todo()

            elif Opcion_Temas == 3:
                
                IDT = input('Ingrese el ID del Tema(Si no se devuelve ningun resultado es porque no existe): ')
                Tema = Temas()
                Tema.consultar_por_id(IDT)

            elif Opcion_Temas == 4:
                
                Ciclo_Temas = False
            
            else:
                
                print('Opcion no valida')

    #---MENU PARA LA SECCION DE VIDEOS---

    elif Opcion_Principal == 2:
        
        Ciclo_Videos = True

        while Ciclo_Videos == True:

            print('---MENU VIDEOS---')
            print('Acciones Disponibles:')
            print('1.-Guardar un Video')
            print('2.-Consultar la informacion de todos los Videos')
            print('3.-Consultar la informacion de un Video por ID')
            print('4.-Regresar al menu principal')

            Opcion_Videos = int(input('Elija el numero de la seccion deseada: '))

            if Opcion_Videos == 1:
                
                V1 = int(input('Ingrese el ID del Video: '))
                V2 = input('Ingrese el nombre del Video: ')
                V3 = input('Ingrese la url del Video: ')
                V4 = input('Ingrese la fecha de publicacion del Video: ')
                Video = Videos(V1, V2, V3, V4)
                Video.guardar()
                print('Guardado con exito')

            elif Opcion_Videos == 2:
                
                print('Desplegando todos los Videos. Ejemplo: ID | NOMBRE DEL VIDEO | URL | FECHA DE PUBLICACION')
                Video = Videos()
                Video.consultar_todo()

            elif Opcion_Videos == 3:
                
                IDV = input('Ingrese el ID del Video(Si no se devuelve ningun resultado es porque no existe): ')
                Video = Videos()
                Video.consultar_por_id(IDV)

            elif Opcion_Videos == 4:
                
                Ciclo_Videos = False
            
            else:
                
                print('Opcion no valida')

    elif Opcion_Principal == 3:
        pass
    elif Opcion_Principal == 4:
        pass
    elif Opcion_Principal == 5:
        pass
    elif Opcion_Principal == 6:
        pass
    
    #---OPCION PARA SALIR DEL MENU PRINCIPAL---

    elif Opcion_Principal == 7:
        
        Ciclo_Principal = False

    else:
        print('Opcion no valida')