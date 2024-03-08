# Собес в Авито
# Похожая задача на 989
"""
Даны два массива, вывести результирующий массив, как сумма этих массивов
 с возможностью перехода десятков

тесты:

arr1 = [1, 2, 4]
arr2 = [9, 4, 6]
res = [1, 0, 7, 0]

arr1 =    [1, 6]
arr2 = [4, 6, 4]

arr1 = [9]
arr2 = [9, 9, 9]
"""

# добавление эл-та через .append и переворот списка по времени О(1) по памяти больше
# reverse создает копию списка и занимает доп память
def sum_arrays_boost(
        arr1: list,
        arr2: list
    ) -> list:
    "function is summarizing two list as math sum"    
    diff_lengths = len(arr1) - len(arr2)
    if diff_lengths:
        if diff_lengths > 0:
            arr2 = [0] * abs(diff_lengths) + arr2
        else:
            arr1 = [0] * abs(diff_lengths) + arr1
    
    # if len(arr1) != len(arr2):
    #     equal_array = []
    #     diff = abs(len(arr2) - len(arr1))
    #     equal_array.extend([0] * diff)
    #     [equal_array.append(x) for x in min(arr1, arr2)]
    #     if len(arr1) < len(arr2):
    #         arr1 = equal_array
    #     elif len(arr1) > len(arr2):
    #         arr2 = equal_array
    res = []
    reserve = 0
    for idx in range(len(arr2)-1, -1, -1):
        res_sum = arr1[idx] + arr2[idx] + reserve
        res.append(res_sum % 10)
        reserve = res_sum // 10
    res.append(reserve)
    
    return res[::-1]

# по времени O(n) по памяти оптимальнее
def sum_arrays_gpt(arr1: list, arr2: list) -> list:
    "function is summarizing two lists as math sum"
    # Pad the shorter list with zeros
    max_length = max(len(arr1), len(arr2))
    arr1 = [0] * (max_length - len(arr1)) + arr1
    arr2 = [0] * (max_length - len(arr2)) + arr2
    
    res = []
    carry = 0
    # Iterate over the arrays from right to left
    for idx in range(max_length-1, -1, -1):
        res_sum = arr1[idx] + arr2[idx] + carry
        # Insert the digit at the beginning of the result list
        res.insert(0, res_sum % 10)
        carry = res_sum // 10
    
    # If there's a carry left, insert it at the beginning
    if carry:
        res.insert(0, carry)

    return res


if __name__ == '__main__':
    print(sum_arrays_boost([9], [9, 9, 9]),
          sum_arrays_boost([1, 2, 4], [9, 4, 6]),
          sum_arrays_boost([1, 6], [4, 6, 4]),
          sum_arrays_boost([], [1, 2])
          )
    # print(sum_arrays_boost([1,2,4],[9,4,6]))

