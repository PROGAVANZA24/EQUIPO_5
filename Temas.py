class Temas:
    
    def __init__(self, id_tema = 0, nombre = ' '):
        self.__id_tema = id_tema
        self.__nombre = nombre

    def guardar(self):
        
        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Archivos_TXT\\Temas.txt', 'a', encoding = 'utf8')
        f.write(f'ID: {self.__id_tema} | TEMA: {self.__nombre}' + '\n')
        f.close 

    def consultar_todo(self):

        f = open('C:\\Archivos_Progra\\PIA\\EQUIPO_5\\Archivos_TXT\\Temas.txt')
        print (f.read())
        f.close