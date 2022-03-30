import numpy as np
from sympy import * #var, Lambda, exp, log, sin, cos, tan, sqrt, ln

teta2, V2 = var('teta2 V2')

class Fluxo_de_carga:
    def __init__(self, Ep, Eq):
        self.Ep = Ep
        self.Eq = Eq
        

    # função para calcular a matriz de admitancia a partir do dicionario de Matriz_Impedancia
    def matriz_admitancia(self, Matriz_Impedancia):
        Y = np.zeros((len(Matriz_Impedancia), len(Matriz_Impedancia)), dtype=complex)
        for i in Matriz_Impedancia: # Elementos fora da diagonal principal
            for j in Matriz_Impedancia[i]:
                if i!=j:
                    try:
                        Y[int(i)-1][int(j)-1] = -1 / Matriz_Impedancia[i][j]
                    except:
                        pass
        for i in Matriz_Impedancia: # Elementos da diagonal Principal
            soma = 0
            for elemento in Matriz_Impedancia[i].values():
                soma += elemento**-1
            Y[int(i)-1][int(i)-1] = soma
        
        self.G = Y.real
        self.B = Y.imag
        print('\nY = ')
        print(np.round(Y,5))
        print('\nG = ')
        print(np.round(self.G,5))
        print('\nB = ')
        print(np.round(self.B,5))
        
        return Y, self.G, self.B

    def define_variaveis(self, Matriz_Barras):
        for i in (Matriz_Barras):
            if ("VT" in Matriz_Barras[i].keys()):
                V1 = Matriz_Barras[i]["VT"][0]
                T1 = Matriz_Barras[i]["VT"][1]
                #P1 = PK()
                #Q1 = QK()
            elif ("PV" in Matriz_Barras[i].keys()):
                V2 = Matriz_Barras[i]["PV"][0]
                T2 = var('T2')
                P2_esp = Matriz_Barras[i]["PV"][2]
                #Q2 = QK()
            elif ("PQ" in Matriz_Barras[i].keys()):
                V3 = var('V3')
                T3 = var('T3')
                P3_esp = Matriz_Barras[i]["PQ"][2]
                Q3_esp = Matriz_Barras[i]["PQ"][3]
        self.V = [V1, V2, V3]
        self.T = [T1, T2, T3]
        self.P_Q_esp = [P2_esp, P3_esp, Q3_esp] 
        
        print('\nV1, V2, V3 = ',self.V)
        print('\nT1, T2, T3 = ',self.T)
        print('\nP_Q_esp = ',self.P_Q_esp)
    
    def matriz_equacoes(self, Matriz_Impedancias):
        self.P_Q = [[0],[0],[0]]
        for k in (Matriz_Impedancias):
            for m in (Matriz_Impedancias[k]):
                Px =  self.V[int(k)-1]*( self.V[int(m)-1]*( self.G[int(k)-1,int(m)-1]*cos(self.T[int(k)-1]-self.T[int(m)-1]) + self.B[int(k)-1,int(m)-1]*cos(self.T[int(k)-1]-self.T[int(m)-1])))
            self.P_Q[int(k)-1] += Lambda((self.T2,self.T3,self.V3),Px)
                

    def formata_matriz(self, M):
        m = len(M) # número de linhas
        n = len(M[0]) # número de colunas
        s = ""
        for i in range(m):
            for j in range(n):
                s += "%9.5f " % M[i][j]
            s += "\n"
        return s

    

    
