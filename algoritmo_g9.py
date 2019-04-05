import numpy as np

def fitness(lista):
    return ((lista[0]-10)**2) + \
        (5*((lista[1]-12)**2)) + \
        (lista[2]**4) + \
        3*((lista[3]-11)**2) + \
        10*(lista[4]**6) + \
        7*(lista[5]**2) + \
        (lista[6]**4) - \
        4*(lista[5] * lista[6]) - \
        10*(lista[5]) - \
        8*(lista[6])

def g1(lista):
    return (-127 + (2 * (lista[0]**2)) + \
        (3 * (lista[1]**4)) + \
        lista[2] + (4 * (lista[3]**2)) + \
        (5 * lista[4]))

def g2(lista):
    return (-282 + (7 * lista[0]) + \
        (3 * lista[1]) + \
        (10*(lista[2]**2)) + \
        lista[3] - lista[4])

def g3(lista):
    return (-196 + (23 * lista[0]) + \
        (lista[1]**2) + \
        (6 * (lista[5]**2)) - \
        (8 * lista[6]))
    
def g4(lista):
    return ((4 * (lista[0]**2)) + \
        (lista[1]**2) - \
        (3 * lista[0] * lista[1]) + \
        (2 * (lista[2]**2)) + \
        (5 * lista[5]) - \
        (11 * lista[6]))

if __name__ == "__main__":
    lista = np.around(np.random.uniform(-10, 10,size=(7)), decimals=2)
    print(lista)
    print("Restricción 1: " + str(g1(lista)))
    print("Restricción 2: " + str(g2(lista)))
    print("Restricción 3: " + str(g3(lista)))
    print("Restricción 4: " + str(g4(lista)))
    print(str(fitness(lista)))