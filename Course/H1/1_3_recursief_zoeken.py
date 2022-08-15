from math import floor

def ZoekRecursief(zoekItem, rij, l, r):
    if l == r:
        if zoekItem == rij[l]:
            return l
        else:
            return -1
    else:
        m = floor ((l+r)/2)
        print(m) # control
        if rij[m] < zoekItem:
            print("look right") # control
            return ZoekRecursief(zoekItem, rij, m + 1, r)
        else:
            print("look left") # control
            return ZoekRecursief(zoekItem, rij, l, m)

#voorbeeld
rij = [1,2,3,4,5,6,7,8,9,10,11,12,13]
l = 0
n = len(rij)
r = n - 1
print(ZoekRecursief(5,rij, l, r)) # 4
print("-------------")

#voorbeeld
l = 0
n = len(rij)
r = n - 1
rij = [1,2,3,4,6,6,7,8,9,10,11,12,13]
print(ZoekRecursief(5,rij,l,r)) # -1