class Empleados:
    
    def __init__(self, id_empleado = 1, nombre = ' ', direccion = ' '):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__direccion = direccion

    def guardar(self):
        
        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Empleados.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_empleado} | NOMBRE: {self.__nombre} | DIRECCION: {self.__direccion}' + '\n')
        f.close

    def consultar_todo(self):

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Empleados.txt')
        print (f.read())
        f.close

    def consultar_por_id(self, id):

        self.id = str(id)

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Empleados.txt')

        for linea in f:
            
            datos = linea.strip().split()
            
            if datos[1] == self.id:
                
                datos = linea.strip().split('|')
                print(datos)

        f.close