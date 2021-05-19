class Cursos:
    
    def __init__(self, id_curso = 0, descripcion = ' ', id_empleado = 0):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado

    def guardar(self):
        
        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Cursos.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_curso} | DESCRIPCION: {self.__descripcion} | EMPLEADO: {self.__id_empleado}' + '\n')
        f.close