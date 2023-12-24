"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List

class Solution(object):
    def two_sum_brutforce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # res = []
        for first in range(len(nums)-1):
            for second in range(first+1, len(nums)):
                if nums[first] + nums[second] == target:
                    return first, second
    
    def two_sum_bp(self, nums, target) -> List[int]:
        
        number_idx = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in number_idx:
                return [number_idx[complement], i]
            number_idx[nums[i]] = i

S = Solution()

print(S.two_sum_bp(nums=[1, 2, 4, 15], target=16))
# assert S.two_sum_bp(nums=[1, 2, 4, 15], target=16) == [0, 3] or [3, 0], print(S.two_sum_bp(nums=[1, 2, 4, 15], target=16))
# assert S.two_sum_bp(nums=[2, 4], target=6) == [0, 1] or [1, 0], print(S.two_sum_bp(nums=[2, 4], target=6))
# assert S.two_sum_bp(nums=[3, 2, 4], target=6) == [1, 2], print(S.two_sum_bp(nums=[3, 2, 4], target=6))