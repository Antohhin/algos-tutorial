"""
Дан бинарный вектор, необходимо написать максимальную длину последовательсти из подряд идущих единиц

тестики:
f([1,1,0,1,1,0]) = 2
f([1,1,0,1,1,1]) = 3
f([1,1,1,1,1,1]) = 6
f([0,0,0]) = 0
f([]) = 0

"""

def max_length_ya(f):
    "calculate maximum length of vector"
    current_length, max_length = 0, 0
    for num in f:
        if num > 0:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length
