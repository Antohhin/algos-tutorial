"""
Задачка с интервью на джун ДС
Написать аналог функции group by
A = [1,2,3,4,5,6,7,8,9,9]
B = ['c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
"""

def groupbysum_get(
        keys: list,
        values:list
        ) -> dict:
    "Dictionary solution"
    # dict_groupby = zip(B, A)
    dct = {}
    for key, value in zip(values, keys): # используй функцию zip(B, A), для итерации по двум спискам одновременно
        dct[key] = dct.get(key, 0) + value
    return dct


A = [1,2,3,4,5,6,7,8,9,9]
B = ['c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
print(groupbysum_get(A, B))