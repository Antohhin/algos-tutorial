#Из курса яндекса
"""

Дан бинарный вектор, необходимо написать максимальную длину
 последовательсти из подряд идущих единиц
тестики:
f([1,0,0,1,0,1]) = 1
f([1,1,0,1,1,0]) = 2
f([1,1,0,1,1,1]) = 3
f([1,1,1,1,1,1]) = 6
f([0,0,0]) = 0
f([]) = 0
"""

def max_vector_seq(f):
    current_length, max_lenght = 0, 0
    for num in f:
        if num > 0:
            current_length += 1
            max_lenght = max(max_lenght, current_length)
        else:
            current_length = 0
    return max_lenght 


assert max_vector_seq([1,0,0,1,0,1]) == 1, print(max_vector_seq([1,0,0,1,0,1]))
assert max_vector_seq([1,1,1,1,1,1]) == 6, print(max_vector_seq([1,1,1,1,1,1]))
assert max_vector_seq([0,0,0]) == 0, print(max_vector_seq([0,0,0]))
assert max_vector_seq([]) == False, print(max_vector_seq([]))

# тестики:
# f([1,0,0,1,0,1]) = 1
# f([1,1,0,1,1,0]) = 2
# f([1,1,0,1,1,1]) = 3
# f([1,1,1,1,1,1]) = 6
# f([0,0,0]) = 0
# f([]) = 0
