class Cursos_Temas_Videos:
    
    def __init__(self, id_CTV = 0, id_CT = 0, id_video = 0):
        self.__id_CTV = id_CTV
        self.__id_CT = id_CT
        self.__id_video = id_video

    def guardar(self):
        
        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Cursos_Temas_Videos.txt', 'a', encoding = 'utf8')
        f.write(f'ID CURSO-TEMA-VIDEO: {self.__id_CTV} | ID CURSO-TEMA: {self.__id_CT} | ID VIDEO: {self.__id_video}' + '\n')
        f.close

    def consultar_todo(self):

        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Cursos_Temas_Videos.txt')
        print (f.read())
        f.close