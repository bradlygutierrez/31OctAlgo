from traceback import print_tb
import Funciones as fun

fun.agregarAsignatura("Español" , 20)
fun.agregarAsignatura("Matematicas" , 90)
fun.agregarEstudiante(1, "Juean", "Lopez", "ISI", fun.notas)

for est in fun.listaEst: 
    print(est.Nombre)
    print(est.Apellidos)
    print(est.Carrera)
    for nota in est.Nota: 
        print(nota.Materia)
        print(nota.Calificacion)