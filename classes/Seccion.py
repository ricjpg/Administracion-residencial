
class Seccion:


    def __init__(self, id, curso, profesor, hora, aula):
        self.id = id
        self.curso = curso
        self.profesor = profesor
        self.hora = hora
        self.aula = aula
        print("objeto Seccion instanciado")

    #def info_seccion(self):
    #    print("la seccion {0}, se imparte en el aula: {1}, en el edificio {2}".format(self.id, self.aula.id, self.edificio.id))