def SelectionSort(a):
    for i in range(len(a)-1,1,-1):
        position = i
        max = a[i]
        for j in range(i-1,-1,-1):
            if a[j] > max:
                position = j
                max = a[j]
        a[position] = a[i]
        a[i] = max
        print(a)
    return a


a = [44,55,12,42,94,18,6,67]
print(a)
print(SelectionSort(a))