"""
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash = {}
        for letter in s:
            hash[letter] = hash.get(letter, 0) + 1
        for letter_t in t:
            if letter_t in hash:
                hash[letter_t] = hash.get(letter_t, 0) - 1
        for count in hash.values():
        # all([value != 0 for value in hash.values()])
            if count != 0:
                return False
        # print(hash)
        return True
        
    def sorting(self, s, t):
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        # for char in range(len(s)):
        return s_sorted == t_sorted

    def isAnagram_ord(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        # Count the frequency of characters in string s
        for x in s:
            count[ord(x) - ord('a')] += 1
            print(ord(x) - ord('a'), count)
        # print()
S = Solution()
# print(S.isAnagram('anagram','nagaram'))
# print(S.isAnagram('rat','cat'))
S.isAnagram_ord('anagram','nagaram')

assert S.isAnagram('anagram','nagaram')==True, print(S.isAnagram('anagram','nagaram'))
assert S.isAnagram('aacc','ccac')==False, print(S.isAnagram('aacc','ccac'))

assert S.sorting('anagram','nagaram')==True, print(S.sorting('anagram','nagaram'))
assert S.sorting('ab','abg')==False, print(S.sorting('ab','abg'))