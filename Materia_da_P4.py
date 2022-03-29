from tkinter.tix import Y_REGION
import numpy as np
from sympy import * #var, Lambda, exp, log, sin, cos, tan, sqrt, ln

teta2, V2 = var('teta2 V2')

class Fluxo_de_carga:
    def __init__(self, Ep, Eq):
        self.Ep = Ep
        self.Eq = Eq
        
        #self.Y = Y
        #self.Delta_P_Q = Delta_P_Q
    
    def formata_matriz(self, M):
        m = len(M) # número de linhas
        n = len(M[0]) # número de colunas
        s = ""
        for i in range(m):
            for j in range(n):
                s += "%9.4f " % M[i][j]
                s += "\n"
        return s

    def Admitancia(self, Y):
        G = Y.real
        B = Y.imag

        print('\nY = %s' % self.formata_matriz(Y))
        print('\nG = \n%s' % self.formata_matriz(G))
        print('\nB = \n%s' % self.formata_matriz(B))

        return G, B

    
