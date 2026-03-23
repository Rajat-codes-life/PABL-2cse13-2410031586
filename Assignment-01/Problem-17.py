def commonElements(a,b,c):

    i=j=k=0
    result=set()

    while i<len(a) and j<len(b) and k<len(c):

        if a[i]==b[j]==c[k]:
            result.add(a[i])
            i+=1
            j+=1
            k+=1

        elif a[i] < b[j]:
            i+=1

        elif b[j] < c[k]:
            j+=1

        else:
            k+=1

    if len(result)==0:
        return [-1]

    return list(result)


arr1=[1,5,10,20,40,80]
arr2=[6,7,20,80,100]
arr3=[3,4,15,20,30,70,80,120]

print(commonElements(arr1,arr2,arr3))