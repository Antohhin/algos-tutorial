"""


"""
from typing import List

def longestConsecutive(nums: List[int]) -> int:
        current_length, max_lenght = 0, 0
        nums_sorted = sorted(nums)
        for idx in range(len(nums)):
            if (nums_sorted[idx] - nums_sorted[idx-1]) == 1:
                current_length += 1
                max_lenght = max(max_lenght, current_length)
            else:
                current_length = 0
        return max_lenght 

print(longestConsecutive(nums=[100,4,200,1,3,2]))