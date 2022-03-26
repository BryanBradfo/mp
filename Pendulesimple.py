import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi


omega_0 = 1
duree = 40 #secondes
dt = 0.01 #secnodes

temps = [dt*k for k in range (1,int(duree/dt+1))]

def euler(theta, theta_point) :
    nouveau_theta=theta+dt*theta_point
    nouveau_theta_point=theta_point+dt*(-omega_0*omega_0)*sin(theta)
    return(nouveau_theta, nouveau_theta_point)

def simule(theta_0, theta_point_0) :
    liste_theta,liste_theta_point=[theta_0],[theta_point_0]
    for k in range (int(duree/dt)-1) :
        L=euler(liste_theta[k],liste_theta_point[k])
        liste_theta.append(L[0])
        liste_theta_point.append(L[1])
    return(liste_theta, liste_theta_point)



"""
plt.plot(temps, simule(0.03,0)[0])
plt.show()
"""

"""
for i in angle :
    plt.plot(temps, simule(i,0)[0])
plt.show()
"""

def euler_harmo(theta, theta_point) :
    nouveau_theta=theta+dt*theta_point
    nouveau_theta_point=theta_point+dt*(-omega_0*omega_0)*theta
    return(nouveau_theta, nouveau_theta_point)

def simule_harmo(theta_0, theta_point_0) :
    liste_theta,liste_theta_point=[theta_0],[theta_point_0]
    for k in range (int(duree/dt)-1) :
        L=euler_harmo(liste_theta[k],liste_theta_point[k])
        liste_theta.append(L[0])
        liste_theta_point.append(L[1])
    return(liste_theta, liste_theta_point)
"""
for i in angle :
    plt.plot(simule_harmo(i,0)[0],simule_harmo(i,0)[1])
plt.show()
"""
def energie(theta, theta_point) :
    return(1/2 * theta_point**2 + omega_0**2*(1-cos(theta)))


angle = [k*0.1 for k in range (20)]

for i in angle :
    L_nrj=[]
    L=simule(i,0) #L=(theta, thetapoint)
    for k in range (len(temps)) :
        L_nrj.append(energie(L[0][k],L[1][k]))
    plt.plot(temps, L_nrj)
plt.show()




