def CardSort(a):
    for i in range(1, len(a), 1):
        x = a[i]
        j = i
        while j > 0 and x < a[j-1]:
            a[j] = a[j-1]
            j = j - 1
        a[j] = x
        print(a)

a = [44,55,12,42,94,18,6,67]
print(a)
print(CardSort(a))