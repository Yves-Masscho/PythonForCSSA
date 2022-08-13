from math import floor

def ZoekRecursief(zoekItem, rij, l, r):
    if l == r:
        if zoekItem == rij[l]:
            return l
        else:
            return -1
    else:
        m = floor ((l+r)/2)
        if rij[m] < zoekItem:
            return ZoekRecursief(zoekItem, rij, m + 1, r)
        else:
            return ZoekRecursief(zoekItem, rij, l, m)

#voorbeeld
rij = [1,2,3,4,5,6]
l = 0
n = len(rij)
r = n - 1
print(ZoekRecursief(5,rij, l, r)) # 4

#voorbeeld
l = 0
n = len(rij)
r = n - 1
rij = [1,2,3,4,6,6]
print(ZoekRecursief(5,rij,l,r)) # -1