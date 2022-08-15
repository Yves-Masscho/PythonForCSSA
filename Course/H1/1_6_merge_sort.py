from math import floor

def MergeSort(a):
    MergeSortRecursive(a,0,len(a) - 1)

def MergeSortRecursive(a, begin, einde):
    if begin < einde:
        midden = floor((begin+einde)/2)
        MergeSortRecursive(a, begin, midden)
        MergeSortRecursive(a, midden+1,einde)
        Merge(a, begin, midden, einde)

def Merge(a, begin, midden, einde):
    i = begin
    j = midden + 1
    k = i
    hulpa = [0]*len(a) # DOESNT WORK YET
    while i <= midden and j <= einde:
        if a[i] <= a[j]:
            hulpa[k] = a[i]
            j = j + 1
        k = k + 1
    if i > midden:
        while j <= einde:
            hulpa[k] = a[j]
            j = j + 1
            k = k + 1
    else:
        while i <= midden:
            hulpa[k] = a[i]
            i = i + 1
            k = k + 1
    for k in range(begin, einde):
        a[k] = hulpa[k]
        



a = [44,55,12,42,94,18,6,67]
print(MergeSort(a))