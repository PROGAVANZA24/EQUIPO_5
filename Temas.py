class Temas:
    
    def __init__(self, id_tema = 0, nombre = ' '):
        self.__id_tema = id_tema
        self.__nombre = nombre

    def guardar(self):
        
        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Temas.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_tema} | TEMA: {self.__nombre}' + '\n')
        f.close 

    def consultar_todo(self):

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Temas.txt')
        print (f.read())
        f.close

    def consultar_por_id(self, id):

        self.id = str(id)

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Temas.txt')
        
        for linea in f:

            datos = linea.strip().split()
            
            if datos[1] == self.id:

                datos = linea.strip().split('|')
                print(datos)

        f.close