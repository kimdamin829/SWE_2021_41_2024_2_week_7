
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []

# Test case
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Output: [0, 1]

nums = [3, 3]
target = 6
print(twoSum(nums, target))  # Output: [0, 1]
