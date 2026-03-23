def mergeArrays(a, b):
    a.extend(b)
    a.sort()

    n = len(a) - len(b)
    b[:] = a[n:]
    a[:] = a[:n]

a = [2,4,7,10]
b = [2,3]

mergeArrays(a,b)

print("a =",a)
print("b =",b)