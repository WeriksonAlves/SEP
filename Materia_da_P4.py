import numpy as np
from sympy import * #var, Lambda, exp, log, sin, cos, tan, sqrt, ln

teta2, V2 = var('teta2 V2')

class Fluxo_de_carga:
    def __init__(self, Barras, Impedancias, Matriz_Barras, Matriz_Impedancias, Ep, Eq):
        self.Barras = Barras
        self.Impedancias = Impedancias
        self.Matriz_Barras = Matriz_Barras
        self.Matriz_Impedancias = Matriz_Impedancias
        self.Ep = Ep
        self.Eq = Eq
    
    def Matriz_Y(self):
        Y = np.zero((self.Barras, self.Barras))
        for i in range(len(self.Barras)):
            for j in range(len(self.Barras)):
                if (i == j):
                    Y[i, j] = 1/self.Impedancias[i]
                Y[i,j] = 1 / self.Matriz_Barras[i,j]
        Y[self.Barras][self.Barras] = -1/(0.01+0.05j)
        y21 = -1/(0.01+0.05j)
        y11 = -y12
        y22 = -y12

        #Matriz de admitância
        Y = np.empty((2), dtype=complex) #ordem da matriz
        Y = np.array([[y11, y12], [y21, y22]])
        G = Y.real
        B = Y.imag
 
