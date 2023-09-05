from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        while k:
            k, a = divmod(k, 10)
            num = [a] + num
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.addToArrayForm(num = [1, 2, 0, 0], k = 34))
