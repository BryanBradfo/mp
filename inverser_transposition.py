
def inverse(T):
    L=len(T)
    S = [i for i in range(L)]
    for i in range (L) :
        S[T[i]] = i
    return(S)

T=[1,0,3,5,4,2]
print(inverse(T))
