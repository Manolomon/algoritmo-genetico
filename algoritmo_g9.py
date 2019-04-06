import numpy as np

POPULATION_SIZE = 200

# region Funciones Matemáticas


def aptitud(lista):
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



if __name__ == "__main__":
    population = list()

    # Población Inicial
    population = [np.around(np.random.uniform(-10, 10, size=(7)), decimals=2) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        print(str(i + 1) + ".- " + str(population[i]))
        print("\tRestricción 1: " + str(g1(population[i])))
        print("\tRestricción 2: " + str(g2(population[i])))
        print("\tRestricción 3: " + str(g3(population[i])))
        print("\tRestricción 4: " + str(g4(population[i])))
        print("\tAptitud: " + str(aptitud(population[i])))

    print("------------------------ Ordenamiento")
    # Orden por aptitud Mínima
    population.sort(key=lambda x: aptitud(x), reverse=False)
    
    for i in range(POPULATION_SIZE):
        print(str(i + 1) + ".- " + str(population[i]))
        print("\tAptitud: " + str(aptitud(population[i])))