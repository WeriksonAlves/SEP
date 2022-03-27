import numpy as np
from sympy import * #var, Lambda, exp, log, sin, cos, tan, sqrt, ln
from math import inf
from fractions import Fraction
import matplotlib.pyplot as plt


# Criar uma classe para calcular o fluxo de carga em sistemas eletricos por meio do metodo de newton-raphson com sistemas de equacoes lineares


class Newton:
    def __init__(self, f, x0, tol=1e-6, nmax=100):
        self.f = f
        self.x0 = x0
        self.tol = tol
        self.nmax = nmax

    def iterate(self):
        x = self.x0
        for i in range(self.nmax):
            fx = self.f(x)
            if fx == 0:
                return x
            dfx = self.f.diff(x)
            if dfx == 0:
                return None
            x = x - fx/dfx
        return None

    
    