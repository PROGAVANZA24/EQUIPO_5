class Empleados:
    
    def __init__(self, id_empleado = 1, nombre = ' ', direccion = ' '):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__direccion = direccion

    def guardar(self):
        
        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Empleados.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_empleado} | NOMBRE: {self.__nombre} | DIRECCION: {self.__direccion}' + '\n')
        f.close