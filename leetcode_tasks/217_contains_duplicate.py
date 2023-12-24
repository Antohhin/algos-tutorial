"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicates = {}
        # counter = 0
        for idx in range(len(nums)):
            # val += duplicates.get(nums[idx], 0)
            # duplicates[nums[idx]] = counter
            # print(duplicates.get(nums[idx], 0))
            # print()
            if nums[idx] in duplicates and duplicates[nums[idx]] >= 1:
                return True
            duplicates[nums[idx]] = duplicates.get(nums[idx], 0) + 1
            # if not duplicates.get(nums[idx], 0):
                # counter = 0
            # if counter >= 2:
                # return True
            # print(duplicates.get(nums[idx], 0))
        # print(duplicates)
        return False
    
    def containsDuplicate_set(self, nums) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            print(seen)
        return False

S = Solution()
# assert S.containsDuplicate(nums=[1,2,3,1]) == True, print(S.containsDuplicate(nums=[1,2,3,1]))
# assert S.containsDuplicate(nums=[1,2,3,4,15,7]) == False, print(S.containsDuplicate(nums=[1,2,3,4,15,7]))

print(S.containsDuplicate_set(nums=[1,2,3,3,4,5,5,5]))