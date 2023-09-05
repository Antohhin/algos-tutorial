"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k
 return the array-form of the integer num + k

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Здесь может быть два подхода:
1. превратить массив с цифрами в число и сложить два числа
2. превратить число в массив и сложить массивы
второй предпочтительнее, на выходе хотим получить тот же массив
"""

class Solution:
    def addToArrayForm(self, num: list, k: int) -> list:
        "function is summarizing integer num and list as math sum"    
        num_k_array = [int(number) for number in str(k)]    # convert integer to array as digit of a number
        diff_lengths = len(num) - len(num_k_array)
        if diff_lengths > 0:
            num_k_array = [0] * diff_lengths + num_k_array
        else:
            num = [0] * abs(diff_lengths) + num

        res = []
        reserve = 0

        for idx in range(len(num)-1, -1, -1):
            res_sum = num[idx] + num_k_array[idx] + reserve
            res.append(res_sum % 10)
            reserve = res_sum // 10
        if reserve:
            res.append(reserve)

        return res[::-1]


if __name__ == '__main__':   
    s = Solution()
    print(s.addToArrayForm(num = [1,2,0,0], k = 34),
          s.addToArrayForm([2, 7, 4], 181),
          s.addToArrayForm([2, 1, 5], 806),
          s.addToArrayForm([], 25)
          )
    