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
rij = [1,2,3,4,5,6,7,8,9,10]
print(ZoekBinair(3,rij))
print(ZoekBinair(5,rij))
print(ZoekBinair(10,rij))
