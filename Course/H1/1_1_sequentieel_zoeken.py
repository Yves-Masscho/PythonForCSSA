def ZoekSequentieel(zoekItem, rij):
    i = 0
    n = len(rij)
    while i < n and rij[i] != zoekItem:
        i = i+1
    if i == n:
        index = -1
    else:
        index = i
    return index

#voorbeeld
rij = [1,2,3,4,5,6]
print(ZoekSequentieel(5,rij)) # 4
#voorbeeld
rij = [1,2,3,4,6,6]
print(ZoekSequentieel(5,rij)) # -1
