

import pylab as pl
import numpy as np
import math as ma

def Euler(F,t0,y0,T,N,i):# F: array -> array (i lignes)
    h=T/N # pas temporel 
    temps=np.linspace(t0,t0+T,N+1) # tableau des temps 
    Y=np.zeros(shape=(i,N+1),dtype=float)# tableau des Y
    Y[:,0]=y0[:] # initialisation (vectorielle)  #garde la 1ere colonne du tableau
    for k in range(0,N):
        Y[:,k+1]=Y[:,k]+h*np.array(F(temps[k],Y[:,k])) #array pour la création d'un tableau 
    return(temps,Y)

def SIR(t,igrec):
    [S,I,R] = igrec # par exemple; 
    # ici, Y stocke 3 scalaires, donc i = 3
    return ([-beta*S*I, beta*S*I - gamma*I,gamma*I])

N=100# nombres de pas
t0=0
T=100 # fin du temps d'étude
S0 = 0.9#valeur à renseigner ( numériques )
I0 = 0.1
R0 = 0
y0=[S0,I0,R0] # conditions initiales 
beta= 0.35
gamma= 0.1

X,Y = Euler(SIR,t0,y0,T,N,3)
pl.plot(Y[0,:],color = 'black') 
pl.plot(Y[1,:],color = 'green')
pl.plot(Y[2,:], color = 'red')

pl.savefig('Trace.pdf')
pl.show()

