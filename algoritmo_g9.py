import numpy as np

def aptitud(lista):
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

if __name__ == "__main__":
    lista = np.around(np.random.uniform(-10, 10,size=(7,)), decimals=2)
    print(lista)
    print(str(aptitud(lista)))