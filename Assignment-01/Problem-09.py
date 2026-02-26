def two_sum(nums, target):
    lookup = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i

# Example
nums = [2, 7, 11, 15]
print(two_sum(nums, 9))