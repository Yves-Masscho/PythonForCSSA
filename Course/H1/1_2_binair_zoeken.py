from math import floor


def ZoekBinair(zoekItem, rij):
    l = 0
    n = len(rij)
    r = n - 1
    while l != r:
        m = floor ((l+r)/2)
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
    
    if rij[l] == zoekItem:
        index = l
    else:
        index = -1
    return index

#voorbeeld
rij = [1,2,3,4,5,6]
print(ZoekBinair(5,rij)) # 4
#voorbeeld
rij = [1,2,3,4,6,6]
print(ZoekBinair(5,rij)) # -1