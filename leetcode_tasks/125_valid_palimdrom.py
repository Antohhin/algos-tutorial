"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # hash map + two pointers?
        if not s:
            return True
        l, r = 0, len(s)-1
        s_lower = s.lower()
        while l < r:
            while r>l and not self.is_alpha_num(s_lower[r]):
                r -= 1
            while l<r and not self.is_alpha_num(s_lower[l]):
                l += 1
            if not s_lower[l] == s_lower[r]:
                return False
            l += 1
            r -= 1
        
        return True

    def is_alpha_num(self, char: str):
        return (ord('A') < ord(char) < ord('Z') or
                ord('a') < ord(char) < ord('z') or
                ord('0') < ord(char) < ord('9'))