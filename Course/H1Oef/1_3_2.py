from math import floor

def zoekBinair(rij,zoekItem):
    l = 0
    n = len(rij)
    r = n - 1
    while l != r:
        print(l,", ",r,sep="")
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