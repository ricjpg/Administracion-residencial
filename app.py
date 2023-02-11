from classes import *

def main():
    
    seccion = Seccion("0701", "OOP", "Uayeb", "0700PM", "1")
    aula1 = Aula("2", "30", seccion)
    floor = Pisos(4, 10, aula1)
    edificio = Edificios("f1", 4)


if __name__ == "__main__":
    main()