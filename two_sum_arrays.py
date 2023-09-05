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

def sum_arrays_boost(
        arr1: list,
        arr2: list
    ) -> list:
    "function is summarizing two list as math sum"    
    diff_lengths = len(arr1) - len(arr2)
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


if __name__ == '__main__':
    print(sum_arrays_boost([9], [9, 9, 9]),
          sum_arrays_boost([1, 2, 4], [9, 4, 6]),
          sum_arrays_boost([1, 6], [4, 6, 4])
          )
    