def isSubset(a,b):

    set_a=set(a)

    for i in b:
        if i not in set_a:
            return False

    return True


a=[11,7,1,13,21,3,7,3]
b=[11,3,7,1,7]

print(isSubset(a,b))