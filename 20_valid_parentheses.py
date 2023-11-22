"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

from icecream import ic

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dct = {')':'(', ']':'[', '}':'{'}
        # dct = {}
        for parentheses in s:
            stack.append(parentheses)
            # dct.setdefault(parentheses, 0)
            if parentheses in dct.keys():
                stack.remove(parentheses)
        # dct.keys()
        return stack#sum(dct.values())# == len(dct.keys())
    # list(lst).

s = '[(a+b)+c]*d*{e-f}'
s1 = '[(a+b)+c*d*{e-f}'
s3 = '()'

valid1 = '()'
valid2 = '))(()))'
valid3 = '{([{}])}'

S = Solution()
ic(S.isValid(valid1))
# ic(S.isValid(s3))
# assert S.isValid(s) == True, ic(S.isValid(s))
# assert S.isValid(s1) == False, ic(S.isValid(s1))