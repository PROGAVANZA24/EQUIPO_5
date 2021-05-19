from Temas import Temas
from Videos import Videos
from Cursos_Temas_Videos import Cursos_Temas_Videos
from Cursos_Temas import Cursos_Temas
from Cursos import Cursos
from Empleados import Empleados

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

    #---MENU CURSOS TEMA VIDEOS---

    elif Opcion_Principal == 3:
        
        Ciclo_Cursos_Temas_Videos = True

        while Ciclo_Cursos_Temas_Videos == True:

            print('---MENU VIDEOS ASIGNADOS A UN VIDEO ASIGNADO A UN TEMA DE UN CURSO---')
            print('Acciones Disponibles:')
            print('1.-Guardar un Video asignado a un Tema de un Curso')
            print('2.-Consultar la informacion de todos los Videos asignados a un Tema de un Curso')
            print('3.-Consultar la informacion de un Video asignado a un Tema de un Curso por ID')
            print('4.-Regresar al menu principal')

            Opcion_Cursos_Temas_Videos = int(input('Elija el numero de la seccion deseada: '))

            if Opcion_Cursos_Temas_Videos == 1:
                
                CTV1 = int(input('Ingrese el ID del Video asignado a un Tema de un Curso: '))
                CTV2 = int(input('Ingrese el ID del Tema asignado al Curso: '))
                CTV3 = int(input('Ingrese el ID del Video: '))
                CurTeVid = Cursos_Temas_Videos(CTV1, CTV2, CTV3)
                CurTeVid.guardar()
                print('Guardado con exito')

            elif Opcion_Cursos_Temas_Videos == 2:
                
                print('Desplegando todos los Videos asignados a un Tema de un Curso.')
                print('Ejemplo: ID CURSO-TEMA-VIDEO | ID CURSO-TEMA | ID VIDEO')
                CurTeVid = Cursos_Temas_Videos()
                CurTeVid.consultar_todo()

            elif Opcion_Cursos_Temas_Videos == 3:
                
                IDVTC = input('Ingrese el ID del Video asignado a un Tema de un Curso(Si no se devuelve ningun resultado es porque no existe): ')
                ViTeCu = Cursos_Temas_Videos()
                ViTeCu.consultar_por_id(IDVTC)

            elif Opcion_Cursos_Temas_Videos == 4:
                
                Ciclo_Cursos_Temas_Videos = False
            
            else:
                
                print('Opcion no valida')

    #---MENU CURSOS TEMAS---

    elif Opcion_Principal == 4:
        
        Ciclo_Cursos_Temas = True

        while Ciclo_Cursos_Temas == True:
            
            print('---MENU TEMAS ASIGNADOS AL CURSO---')
            print('Acciones Disponibles:')
            print('1.-Guardar un Tema asignado a un Curso')
            print('2.-Consultar la informacion de todos los Temas asignados a un Curso')
            print('3.-Consultar la informacion de un Tema asignado a un Curso por ID')
            print('4.-Regresar al menu principal')

            Opcion_Cursos_Temas = int(input('Elija el numero de la seccion deseada: '))

            if Opcion_Cursos_Temas == 1:
                
                CT1 = int(input('Ingrese el ID del Tema asignado a un Curso: '))
                CT2 = int(input('Ingrese el ID del Curso: '))
                CT3 = int(input('Ingrese el ID del Tema: '))
                CurTe = Cursos_Temas(CT1, CT2, CT3)
                CurTe.guardar()
                print('Guardado con exito')

            elif Opcion_Cursos_Temas == 2:
                
                print('Desplegando todos los Videos asignados a un Tema de un Curso.')
                print('Ejemplo: ID CURSO-TEMA | ID CURSO | ID TEMA')
                CurTe = Cursos_Temas()
                CurTe.consultar_todo()

            elif Opcion_Cursos_Temas == 3:
                
                IDCT = input('Ingrese el ID del Tema asignado a un Curso(Si no se devuelve ningun resultado es porque no existe): ')
                TeCu = Cursos_Temas()
                TeCu.consultar_por_id(IDCT)

            elif Opcion_Cursos_Temas == 4:
                
                Ciclo_Cursos_Temas = False
            
            else:
                
                print('Opcion no valida')

    #---MENU CURSOS---

    elif Opcion_Principal == 5:
        
        Ciclo_Cursos = True

        while Ciclo_Cursos == True:

            print('---MENU CURSOS---')
            print('Acciones Disponibles:')
            print('1.-Guardar un Curso')
            print('2.-Consultar la informacion de todos los Cursos')
            print('3.-Consultar la informacion de un Curso por ID')
            print('4.-Regresar al menu principal')

            Opcion_Cursos = int(input('Elija el numero de la seccion deseada: '))

            if Opcion_Cursos == 1:
                
                C1 = int(input('Ingrese el ID del Curso: '))
                C2 = input('Ingrese la descripcion del Curso: ')
                C3 = int(input('Ingrese el ID del Empleado: '))
                Curso = Cursos(C1, C2, C3)
                Curso.guardar()
                print('Guardado con exito')

            elif Opcion_Cursos == 2:
                
                print('Desplegando todos los Cursos. Ejemplo: ID CURSO | DESCRIPCION | ID EMPLEADO')
                Curso = Cursos()
                Curso.consultar_todo()

            elif Opcion_Cursos == 3:
                
                IDC = input('Ingrese el ID del Curso(Si no se devuelve ningun resultado es porque no existe): ')
                Curso = Cursos()
                Curso.consultar_por_id(IDC)

            elif Opcion_Cursos == 4:
                
                Ciclo_Cursos = False
                
            else:
                print('Opcion no valida')

    #---MENU EMPLEADOS---

    elif Opcion_Principal == 6:
        
        Ciclo_Empleados = True

        while Ciclo_Empleados == True:

            print('---MENU EMPLEADOS---')
            print('Acciones Disponibles:')
            print('1.-Guardar un Empleado')
            print('2.-Consultar la informacion de todos los Empleados')
            print('3.-Consultar la informacion de un Empleado por ID')
            print('4.-Regresar al menu principal')

            Opcion_Empleados = int(input('Elija el numero de la seccion deseada: '))

            if Opcion_Empleados == 1:
                
                E1 = int(input('Ingrese el ID del Empleado: '))
                E2 = input('Ingrese el nombre del Empleado: ')
                E3 = input('Ingrese la direccion del Empleado: ')
                Empleado = Empleados(E1, E2, E3)
                Empleado.guardar()
                print('Guardado con exito')

            elif Opcion_Empleados == 2:
                
                print('Desplegando todos los Cursos. Ejemplo: ID EMPLEADO | NOMBRE | DESCRIPCION')
                Empleado = Empleados()
                Empleado.consultar_todo()

            elif Opcion_Empleados == 3:
                
                IDE = input('Ingrese el ID del Empleado(Si no se devuelve ningun resultado es porque no existe): ')
                Empleado = Empleados()
                Empleado.consultar_por_id(IDE)

            elif Opcion_Empleados == 4:
                
                Ciclo_Empleados = False
            
            else:
                
                print('Opcion no valida')
    
    #---OPCION PARA SALIR DEL MENU PRINCIPAL---

    elif Opcion_Principal == 7:
        
        Ciclo_Principal = False

    #---MENSAJE DE ERROR DE OPCION INVALIDA---
    
    else:
        print('Opcion no valida')