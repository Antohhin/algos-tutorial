"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Попробовать сделать если нужно от строки отрезать все не буквы, знаки препинания

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
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dct = {')':'(', ']':'[', '}':'{'}
        # dct = {}
        for parentheses in s:
            # dct.setdefault(parentheses, 0)
            if parentheses in dct.values():
                stack.append(parentheses)
            elif parentheses in dct.keys():
                # ic(stack)
                # open_bracket = dct.get(parentheses)
                if stack and stack[-1] == dct.get(parentheses):
                    stack.pop()  
                else:
                    return False
                # if closing_bracket in stack:
                # ic(closing_bracket)
                # stack.remove(parentheses)
        # dct.keys()
        return len(stack) == 0#sum(dct.values())# == len(dct.keys())
    # list(lst).

s = '[(a+b)+c]*d*{e-f}'
s1 = '[(a+b)+c*d*{e-f}'
s3 = '()'

valid1 = '()'
valid2 = '))(()))'
valid3 = '{([{}])}'
s4 = "([)]"

S = Solution()

assert S.isValid(s) == True, ic(S.isValid(s))
assert S.isValid(s1) == False, ic(S.isValid(s1))

class Solution_bp(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dict = {")": "(", "}": "{", "]": "["}
        stack=[]
        for bracket in s:
            if bracket in my_dict.values():
               stack.append(bracket)
            elif bracket in my_dict.keys(): #
                if not stack or stack.pop() != my_dict[bracket]: # использовать pop
                    return False
        return not stack            

S = Solution_bp()
ic(S.is_valid(valid1))
ic(S.is_valid(valid2))
ic(S.is_valid(valid3))
ic(S.is_valid(s4))
