def tripletSum(arr,target):

    arr.sort()
    n=len(arr)

    for i in range(n-2):

        left=i+1
        right=n-1

        while left<right:

            s=arr[i]+arr[left]+arr[right]

            if s==target:
                return True

            elif s<target:
                left+=1
            else:
                right-=1

    return False


arr=[1,4,45,6,10,8]
target=13

print(tripletSum(arr,target))