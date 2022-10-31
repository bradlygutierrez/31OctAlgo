
from re import I
import Estructura
listaEst = []
notas = []    
def agregarEstudiante(id,nom,ape,car,notas):
    est = Estructura.Estudiante(id,nom,ape,car,notas)
    listaEst.append(est)

def agregarAsignatura(materia, nota):
    nota = Estructura.Nota(materia, nota)
    notas.append(nota)

def calcularPromedio():
    suma = 0
    for nota in notas:
        suma += nota.Calificacion
    promedio = suma /len(notas)
    return promedio

def calcularPrimerosLugares():
    i = 0
    while(i < len(listaEst)):
        j = i + 1
        while (j < len(listaEst)):
            est1 = listaEst[i]
            est2 = listaEst[j]
            prom1 = calcularPromedio(est1.Notas)
            prom2 = calcularPromedio(est2.Notas)
            if(prom2 > prom1):
                aux = listaEst[i]
                listaEst[i] = listaEst[j]
                listaEst[j] = aux
            j += 1
        i += 1
    return listaEst[0], listaEst[1], listaEst[2]