class Videos:

    def __init__(self, id_video = 0, nombre = ' ', url = ' ', fecha_publicacion = ' '):
        self.__id_video = id_video
        self.__nombre = nombre
        self.__url = url
        self.__fecha_publicacion = fecha_publicacion

    def guardar(self):
        
        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Videos.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_video} | TEMA: {self.__nombre} | URL: {self.__url} | FECHA DE PUBLICACION: {self.__fecha_publicacion}' + '\n')
        f.close

    def consultar_todo(self):

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Videos.txt')
        print (f.read())
        f.close