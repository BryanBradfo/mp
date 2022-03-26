
from math import *


def pomme():
    x0 = 6
    while True:
        xN = x0*(2-log(x0))
        if abs((xN-x0)/xN) <= 1e-15:
            return xN
        else:
            x0 = xN

print(pomme())
print(exp(1))

"""

def myst(* data ) :
    x = [d [0] for d in data ]
    y = [d [1] for d in data ]
    data_len = len ( data )
    result_x = sum (x ) / data_len
    result_y = sum (y ) / data_len
    return [ result_x , result_y ]

print(myst((100 , 0) , (0 , 0) , (100 , 100) , (0 , 50)))
"""

'''
def  f(x) :
    i = 0
    j = 0
    k = len(x) − 1
    while (i <= k ) :
        if ( x[ i ] == 0 ) :
            x[i] , x[j] = x[j] , x[i]
            j+=1
            i+=1
        elif ( x[i] == 1 ) :
            x [ i ] = x [ k ]
            x [ k ] = 1
            k−=1
        else :
            i+=1
'''
