from msilib.schema import Class


class Estudiante: 
    def __init__(self, id, nom, ape, carrera, notas):
        self.Id = id
        self.Nombre = nom
        self.Apellidos = ape
        self.Carrera = carrera
        self.Nota = notas
        
    
class Nota: 
    def __init__(self, materia, cali):
        self.Materia = materia
        self.Calificacion = cali