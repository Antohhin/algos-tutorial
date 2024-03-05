"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

f([4, 3, 3, 2, 1, 1]) -> f([1, 1, 2, 3, 3, 4]) -> [1, 3]

Пригодится ли тут сортировка массива?
Пригодится ли хэш-таблица?
Как лушче перебрать массив с начала или с конца?
Точно сортировка

Группировка всех интов
1. Создаю хэш таблицу
2. Наполняю key: unique num, value: count num
3. возвращаю первые k value
"""
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    store = {}
    for key in nums:
        store[key] = store.get(key, 0) + 1
    sorted_store = dict(sorted(store.items(), key = lambda x:x[1]))
    return list(sorted_store.keys())[-k:]
        
        # if not num in store:
            # 
            # duplicates[nums[idx]] = duplicates.get(nums[idx], 0) + 1
            # dct[key] = dct.get(key, 0) + value

from collections import defaultdict

# Vanya Lipatov's solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Vanya Solution
        # Наполнение словаря key: uniq num, value: count
        # {4: 1, 3: 2, 2: 1, 1: 2}
        freqs = defaultdict(int) # O(n) memory
        for num in nums:
            freqs[num] += 1
        # Переворот словаря где value: key
        # {1: [4, 2], 2: [1, 3]}
        inv_freqs = defaultdict(list) # O(1) memory
        for key, value in freqs.items():
            inv_freqs[value].append(key)
        # Итерация с конца по ключам
        res = []
        for n in range(len(nums), 0, -1):
            # n = 6, n = 5, n = 4
            # {1: [4, 2], 2: [3, 1], 6: [], 5: [], 4: []}
            # поиск существующих значений из списка
            # при не совпадении создается пустой список как значение в defaultdict
            # при совпадении, возвращаются значение (ключи словаря freq)
            for num in inv_freqs[n]:
                res.append(num)
                if len(res) == k:
                    return res

nums = [4, 3, 3, 2, 1, 1]
S = Solution()
S.topKFrequent(nums, k=2)
assert S.topKFrequent(nums, k=2) == [1, 3] or [3, 1], print(S.topKFrequent(nums, k=2))
