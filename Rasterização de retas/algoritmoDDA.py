import matplotlib.pyplot as plt
import numpy as np
import math


def plot_coord(matrix):
    figure = plt.figure()
    axes = figure.add_subplot(111)

    c_axes = axes.matshow(matrix, interpolation='nearest')
    figure.colorbar(c_axes)

    plt.show()
      
def create_fragment(x):
    x_m = math.floor(x)
    return x_m,


def reta1(x1, y1, x2, y2, mult=1,):
    
    x1 = x1*mult
    x2 = x2*mult
    y1 = y1*mult
    y2 = y2*mult
    
    x, y = x1, y1
    if(abs(x2-x1) >= abs(y2-y1)):
        tamanho = abs(x2-x1);
    else:
        tamanho = abs(y2-y1);

    dx = (x2 - x1) / float(tamanho)
    dy = (y2 - y1) / float(tamanho)
    matrix = np.zeros((tamanho*2, tamanho*2))

    matrix[create_fragment(y)][create_fragment(x)] = 5
    for i in range(tamanho):
        x += dx
        y += dy
        matrix[create_fragment(y)][create_fragment(x)] = 5

    return matrix

def reta2(x1, y1, x2, y2,matrix):
    x, y = x1, y1
    if(abs(x2-x1) >= abs(y2-y1)):
        tamanho = abs(x2-x1);
    else:
        tamanho = abs(y2-y1);

    dx = (x2 - x1) / float(tamanho)
    dy = (y2 - y1) / float(tamanho)
    matrix[create_fragment(y)][create_fragment(x)] = 4
    for i in range(tamanho):
        x += dx
        y += dy
        matrix[create_fragment(y)][create_fragment(x)] = 4

    return matrix

def reta3(x1, y1, x2, y2,matrix):
    x, y = x1, y1
    if(abs(x2-x1) >= abs(y2-y1)):
        tamanho = abs(x2-x1);
    else:
        tamanho = abs(y2-y1);

    dx = (x2 - x1) / float(tamanho)
    dy = (y2 - y1) / float(tamanho)
    matrix[create_fragment(y)][create_fragment(x)] = 3
    for i in range(tamanho):
        x += dx
        y += dy
        matrix[create_fragment(y)][create_fragment(x)] = 3

    return matrix
    
if __name__ == '__main__':
    i = 1 #inicializador
    while i <= 3:
        matrix = reta1(2, 4, 4, 11,i)
        matrix = reta2(3, 2, 12, 7,matrix)
        matrix = reta3(0,0,9,3,matrix)
        plot_coord(matrix)
        i=i+1