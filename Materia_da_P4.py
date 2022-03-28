import numpy as np
from sympy import * #var, Lambda, exp, log, sin, cos, tan, sqrt, ln
#from math import inf
#from fractions import Fraction
#import matplotlib.pyplot as plt
teta2, V2 = var('teta2 V2')

class Fluxo_de_carga:
    def __init__(self, Y, G, B, y, x, J, x0, e):
        self.Y = Y
        self.G = G
        self.B = B
        self.y = y
        self.x = x
        self.J = J
        self.x0 = x0
        self.e = e

        print('\nY = ', Y)
        print('\nG = ', G)
        print('\nB = ', B)

        self.equações()
        self.metodo_newton()

    def equações(self):
        print('\n')

        for i in range(len(self.y)):
            print('y[',i,'] = ', self.y[i])
        print('\n')

        for i in range(len(self.x)):
            print('x[',i,'] = ', self.x[i])
        print('\n')

        for i in range(len(self.J)):
            for j in range(len(self.J)):
                print('J[',i,'][',j,'] = ', self.J[i][j])
        print('\n')

    def metodo_newton(self):
        
    

        #criar uma função para calcular o metodo de newton para um sistema de equações
        def F(x):
            return np.dot(J, x) - y

        def Fd(x):
            return J

        def main():
            dados = {'n____':[],
                     'Xn___':[],
                     'e_abs':[],
                     'e_rel':[],
                     'Fxn__':[],
                     'FDxn_':[]}
            n = 0
            dados['n____'].append(n)

            #Dados
            print('Entrada dos parâmetros:')
            x0 = self.x0



    #def Newton()
        
        




    
    
        
