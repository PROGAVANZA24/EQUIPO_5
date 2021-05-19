class Cursos_Temas:
    
    def __init__(self, id_CT = 0, id_curso = 0, id_tema = 0):
        self.__id_CT = id_CT
        self.__id_curso = id_curso
        self.__id_tema = id_tema

    def guardar(self):
        
        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Cursos_Temas.txt', 'a', encoding = 'utf8')
        f.write(f'ID CURSO-TEMA: {self.__id_CT} | ID CURSO: {self.__id_curso} | ID TEMA: {self.__id_tema}' + '\n')
        f.close

    def consultar_todo(self):

        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Cursos_Temas.txt')
        print (f.read())
        f.close

    def consultar_por_id(self, id):

        self.id = str(id)

        f = open('C:\\Users\\richa\\Desktop\\PIA_Prueba\\Archivos de Texto\\Cursos_Temas.txt')

        for linea in f:
            
            datos = linea.strip().split()
            
            if datos[2] == self.id:
                
                datos = linea.strip().split('|')
                print(datos)

        f.close