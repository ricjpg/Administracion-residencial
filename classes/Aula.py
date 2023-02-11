from classes import Seccion
class Aula:

    def __init__(self, id, cantidadMaxima, seccion):

        self.id = id
        self.cantidadMaxima = cantidadMaxima
        self.seccion = seccion
        print("objeto aula instanciado")

        print("id del aula: {0}\ncantidad max de alumnos {1}\nnombre del curso: {2}\nhora asignada: {3}\nProfesor: {4}".format(self.id, self.cantidadMaxima, self.seccion.curso, self.seccion.hora, self.seccion.profesor))
