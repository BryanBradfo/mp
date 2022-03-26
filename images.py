# Ne pas modifier ########################

import inspect
import os

os.chdir(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))

##### À vous

import numpy as np
from PIL import Image

victoire = Image.open("colibri.jpg")

r,g,b=victoire.split()

array_r=np.array(r)

'''for y in range(100,200):
    for x in range(100,200):
        array_r[y][x]=255-array_r[y][x]


Image.merge("RGB",[Image.fromarray(array_r),g,b]).show()
'''

def demi_tour(image):
    taille=image.size
    res=np.zeros_like(image)
    tab=np.array(image)
    for i in range(taille[1]): #indice des lignes
        for j in range(taille[0]): #indice des colonnes
            res[i][j]=tab[taille[1]-i-1][taille[0]-j-1]
    im=Image.fromarray(res).show()
    return(im)


def negatif(image):
    taille=image.size
    tab=np.array(image)
    for i in range(taille[1]):
        for j in range(taille[0]):
            tab[i][j]=np.array([255,255,255])-tab[i][j]
    im=Image.fromarray(tab)
    return(im)


def gris(image):
    taille=image.size
    tab=np.array(image)
    res=np.zeros((taille[1],taille[0]), dtype=np.uint8)
    for i in range(taille[1]):
        for j in range(taille[0]):
            res[i][j]=0.2126*tab[i][j][0]+0.7152*tab[i][j][1]+0.0722*tab[i][j][2]
    im=Image.fromarray(res)
    return(im)
"""
def gris(tablo) :
    h,l = len(tablo), len(tablo[0])
    tablo2 =np.zeros((h,l), dtype = np.uint8)
    for y in range(h) :
        for x in range(l) :
            tablo2[y][x] = 0.

def aux(m,c,x,y):
    #print(m)
    #print(c)
    res=0
    for i in range(-1,2):
        for j in range(-1,2):
            res+=m[x+i][y+j]*c[1-i,1-j]
    return(res)

def convolution(m,c):
    tab=np.array(m)
    taille=m.size
    res=np.zeros_like(tab)
    for i in range(1,taille[1]-1):
        for j in range(1,taille[0]-1):
            b=aux(tab,c,i,j)
            if b<0:
                res[i][j]=0
            elif b>255:
                res[i][j]=255
            else:
                res[i][j]=b
    im=Image.fromarray(res).show()
    return(im)
"""
def produit_c(m,c,x,y) :
    L = [-1,0,1]
    r = 0
    for i in L :
        for j in L :
            r += c[1-i][1-j]*m[y+i][x+j]
    if r < 0 :
        r = 0
    if r > 255 :
        r = 255
    return(r)

def convolution(m,c) :
    h,l = len(m),len(m[0])
    tablo2 = np.zeros((h,l), dtype =np.uint8)
    for y in range(1,h-1) :
        for x in range(1,l-1) :
            tablo2[y][x] = produit_c(m,c,x,y)
    Image.fromarray(tablo2).show()

C = np.array([[(1/9) for k in range(3)] for k in range(3)])
print(len(C[0]))
"""
B = np.array([0,-1.0],[-1.5,-1],[0,-1.0])
"""
matrice=np.array([[1/9.,1/9.,1/9.],[1/9.,1/9.,1/9.],[1/9.,1/9.,1/9.]])

contraste=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])



