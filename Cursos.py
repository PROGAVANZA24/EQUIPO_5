class Cursos:
    
    def __init__(self, id_curso = 0, descripcion = ' ', id_empleado = 0):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado

    def guardar(self):
        
        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Cursos.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_curso} | DESCRIPCION: {self.__descripcion} | EMPLEADO: {self.__id_empleado}' + '\n')
        f.close

    def consultar_todo(self):

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Cursos.txt')
        print (f.read())
        f.close

    def consultar_por_id(self, id):

        self.id = str(id)

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Cursos.txt')

        for linea in f:
            
            datos = linea.strip().split()
            
            if datos[1] == self.id:
                
                datos = linea.strip().split('|')
                print(datos)

        f.close