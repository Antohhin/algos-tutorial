"""
Написать аналог random choice с повторами
"""
import random

# бинарный поиск нужен, чтобы найти индекс диапазона в котором лежит эл-т
def binary_search(cumsum_arr, target):
    left, right = 0, len(cumsum_arr) - 1
    while left < right:
        mid = (left + right) // 2
        if cumsum_arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
# кумулятивная сумма для того чтобы уложить вероятности в диапазон в котором буду искать рандомное число
def cumsum(arr):
    cumsum = []
    current_sum = 0
    for num in arr:
        current_sum += num
        cumsum.append(current_sum)
    return cumsum

def sample(arr, size):
    probs = [num[1] for num in arr] # разложить вероятности в список из вложенного списка
    cumsum_arr = cumsum(probs)
    
    results = []
    for _ in range(size): 
        # чтобы быть уверенным что значение попадет в диапазон кумулятивных сумм
        r = random.random() * cumsum_arr[-1]  # Scale random number by total sum of probabilities
        idx = binary_search(cumsum_arr, r)
        results.append(arr[idx][0])
    return results

arr = [['a', 0.1], ['b', 0.1], ['c', 0.7]]
print(sample(arr, size=10))

