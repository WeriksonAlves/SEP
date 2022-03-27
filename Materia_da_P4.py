import numpy as np
from sympy import * #var, Lambda, exp, log, sin, cos, tan, sqrt, ln
from math import inf
from fractions import Fraction
import matplotlib.pyplot as plt


class Fluxo_de_carga:
    def __init__(self, Barras, res, rea):
        self.n = Barras
        self.r = res
        self.x = rea
        #self.yf = yf
        #self.n = n
        #self.x = np.linspace(x0, xf, n)
        #self.y = np.linspace(y0, yf, n)

    

