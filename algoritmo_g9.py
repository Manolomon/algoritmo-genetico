import numpy as np
import csv
import sys

POPULATION_SIZE = 200
evaluaciones = 0

class Individuo:
        aptitud = 0.0
        solucion = list()

# region Funciones Matemáticas

def aptitud(lista):
    global evaluaciones
    evaluaciones = evaluaciones + 1
    if not (g1(lista) and g2(lista) and g3(lista) and g4(lista)):
        return 1000000000.00
    else:
        return (((lista[0]-10)**2)
                + (5 * ((lista[1]-12)**2))
                + (lista[2]**4)
                + 3 * ((lista[3]-11)**2)
                + 10 * (lista[4]**6)
                + 7 * (lista[5]**2)
                + (lista[6]**4)
                - 4 * (lista[5] * lista[6])
                - 10 * (lista[5])
                - 8 * (lista[6]))

def g1(lista):
    return (-127 + (2 * (lista[0]**2))
        + (3 * (lista[1]**4))
        + lista[2] + (4 * (lista[3]**2))
        + (5 * lista[4])) <= 0

def g2(lista):
    return (-282 + (7 * lista[0])
        + (3 * lista[1])
        + (10*(lista[2]**2))
        + lista[3] - lista[4]) <= 0

def g3(lista):
    return (-196 + (23 * lista[0])
        + (lista[1]**2)
        + (6 * (lista[5]**2))
        - (8 * lista[6])) <= 0

def g4(lista):
    return ((4 * (lista[0]**2))
        + (lista[1]**2)
        - (3 * lista[0] * lista[1])
        + (2 * (lista[2]**2))
        + (5 * lista[5])
        - (11 * lista[6])) <= 0

# endregion

# region Funciones algoritmo genetico
def seleccion(poblacion):
    if (len(poblacion) <= 20):
        return poblacion
    else:
        padres = list()
        for i in range(0, len(poblacion), 2):
            if (poblacion[i].aptitud < poblacion[i+1].aptitud):
                padres.append(poblacion[i])
            else:
                padres.append(poblacion[i+1])
        return seleccion(padres)
    
def cruza(padres):
    solucionHijoA = list()
    solucionHijoB = list()
    hijos = list()
    hijoA = Individuo()
    hijoB = Individuo()
    for i in range(0,20,2):
        solucionHijoA.clear()
        solucionHijoB.clear()
        for j in range(4):
            solucionHijoA.append(padres[i].solucion[j])
            solucionHijoB.append(padres[i+1].solucion[j])
        for j in range(4,8):            
            hijo = round((padres[i].solucion[j]*0.5)+(padres[i+1].solucion[j]*0.5),2)
            solucionHijoA.append(hijo)
            solucionHijoB.append(hijo)
        hijoA.solucion = solucionHijoA
        hijoB.solucion = solucionHijoB
        hijos.append(hijoA)
        hijos.append(hijoB)
    return hijos        

def mutacion(hijos):
    hijosMutados = list()
    for i in range(len(hijos)):
        posicion = np.random.randint(1,8)
        hijos[i].solucion[posicion] = np.around(np.random.uniform(-10, 10),decimals=3)
        hijos[i].aptitud = (aptitud(hijos[i].solucion))
        hijosMutados.append(hijos[i])
    return hijosMutados

# endregion

def imprimir(ejecucion, population, gen):
    with open(str(ejecucion) + "output.csv", "a") as file:
        writer = csv.writer(file, delimiter=',')
        for i in range(len(population)):
            atk = population[i].aptitud
            listat = [gen, atk]
            writer.writerow(listat)
        file.close()

if __name__ == "__main__":
    population = list()
    mejor = Individuo()
    ejecucion = sys.argv[1]
    generacion = 1
    padres = list()
    # Población Inicial
    with open(str(ejecucion) + "output.csv", "a") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["generacion", "aptitud"])
        file.close()

    for _ in range(POPULATION_SIZE):
        individuo = Individuo()
        individuo.solucion = np.around(np.random.uniform(-10, 10, size=(8)),decimals=3)
        print(individuo.solucion)
        individuo.aptitud = aptitud(individuo.solucion)
        population.append(individuo)

    print("------------------------ Ordenamiento")
    # Orden por aptitud Mínima
    population.sort(key=lambda x: x.aptitud, reverse=False)

    imprimir(ejecucion, population, generacion)
    
    for i in range(POPULATION_SIZE):
        print(str(i + 1) + ".- " + str(population[i].solucion))
        print("\tAptitud: " + str(population[i].aptitud))

    mejor = population[0]
    print("Mejor generacion " + str(generacion))
    print("\t " + str(mejor.solucion))
    print("Aptitud: " + str(mejor.aptitud))

    while (population[0].aptitud != 0 and evaluaciones < 220000):                
        padres.clear()
        mejor = population[0]
        # print("------------------------ Seleccion de padres")
        for i in range (160):
                padres.append(population[i])
        padres = seleccion(padres)

        # print("------------------------ Cruza y mutacion")
        hijos = cruza(padres)
        hijos = mutacion(hijos)
        
        population = population + hijos
        
        population.sort(key=lambda x: x.aptitud, reverse=False)
        del population[-20:]
        print("Mejor generacion " + str(generacion))
        print("\t " + str(mejor.solucion))
        print("Aptitud: " + str(mejor.aptitud))
        generacion = generacion + 1
        imprimir(ejecucion, population, generacion)
