def minJumps(arr):
    n = len(arr)

    if arr[0] == 0:
        return -1

    jumps = 0
    farthest = 0
    end = 0

    for i in range(n-1):
        farthest = max(farthest, i + arr[i])

        if i == end:
            jumps += 1
            end = farthest

            if end >= n-1:
                return jumps

    return -1


arr = [1,3,5,8,9,2,6,7,6,8,9]
print(minJumps(arr))