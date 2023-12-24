"""
Найти строку в которой скобки (){}[] верно расставлены,
либо порядковый номер первой ошибочной скобки

Если скобки в s расставлены правильно, выведите
строку “Success". В противном случае выведите индекс (используя индексацию с единицы)
 первой закрывающей скобки, для
которой нет соответствующей открывающей. Если такой нет,
выведите индекс первой открывающей скобки, для которой нет
соответствующей закрывающей.

{[} -> 2
((({[]}) -> 2
{}([] -> 3
(slkj, {lk[lve]} ,l) -> Success
(slkj{lk[lsj]} -> 1
dasdsadsadas]]] -> 13
"""


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dict = {")": "(", "}": "{", "]": "["}
        stack=[]
        for idx, bracket in enumerate(s):
            if bracket in my_dict.values():
               stack.append([bracket, idx + 1])
            elif bracket in my_dict.keys(): #
                # if not stack or stack.pop()[0] != my_dict[bracket]: # использовать pop
                #     return False
                if not stack or stack.pop()[0] != my_dict[bracket]:
                    return stack[-1][1]
        # if not stack:
            # return 'Success'
        if not stack:
            return 'Success'
        return stack[-1][1]
                # if stack and stack[-1] == my_dict.get(bracket):
                    # stack.pop()  
                # else:
                    # return stack[-1][1]
                    # return False
        # return not stack 
    

S = Solution()

s1 = '{[b}'# -> 2
s2 = '((({[]})'# -> 2
s3 = '{}([]'# -> 3
s4 = '(slkj, {lk[lve]} ,l)'# -> Success
s5 = '(slkj{lk[lsj]}'# -> 1
s6 = 'dasdsadsadas]]]'# -> 13

print(S.is_valid(s1))
print(S.is_valid(s2))
print(S.is_valid(s3))
print(S.is_valid(s4))
print(S.is_valid(s5))
print(S.is_valid(s6))








