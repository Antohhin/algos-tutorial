"""
Имеем список целых чисел. Нужно перенести все нули в конец 
списка, сохраняя порядок ненулевых эл-ов

тестики:
f([1,2,3,0,0,4,0,5]) = [1,2,3,4,5,0,0,0]
f([0,0,0,1,2,5]) = [1,2,5,0,0,0]
f([0,0,0,0,0,1]) = [1,0,0,0,0,0]
f([0,1,2,3,4,0]) = [1,2,3,4,0,0]

"""
from icecream import ic

def shift_zeros(nums: list) -> list:
    # while n != len(nums):
    # for i in nums:
    #     if i == 0:
    #         zero_num = nums.pop(i)
    #         nums.append(zero_num)
    # return nums
    zero_idx = None
    for idx in range(len(nums)):
        if nums[idx] == 0:    
            if nums[idx-1] != 0:
                zero_idx = idx
        else:
            if zero_idx != None:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
    return nums
    # zeros = 0
    # for i in range(nums):
    #     if nums[i] == 0:
    #         zero_idx = i
    #         nums.pop(zero_idx)
    #     else:
    #       pass
    # # for idx, i in enumerate(nums):
    #     k = 0
    #     if i != 0:
    #         pass
    #     else:
    #         k += 1
    #         nums.pop(idx)
    # return
            # zero_num = nums.pop(idx)
            # nums.append(zero_num)


def correct_shift_zeros(nums: list) -> list:
    zero_idx = None
    for idx in range(len(nums)):
        if (nums[idx] == 0) and (zero_idx is None):    
            zero_idx = idx
        if (zero_idx != None) and (nums[idx] != 0):
            nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
            zero_idx += 1
    return nums


# assert shift_zeros([1,2,3,0,0,4,0,5]) == [1,2,3,4,5,0,0,0], ic(shift_zeros([1,2,3,0,0,4,0,5]))
# assert shift_zeros([0,0,0,1,2,5]) == [1,2,5,0,0,0], ic(shift_zeros([0,0,0,1,2,5]))
# assert shift_zeros([0,0,0,0,0,1]) == [1,0,0,0,0,0], ic(shift_zeros([0,0,0,0,0,1]))
# assert shift_zeros([0,1,2,3,4,0]) == [1,2,3,4,0,0], ic(shift_zeros([0,1,2,3,4,0]))


assert correct_shift_zeros([1,2,3,0,0,4,0,5]) == [1,2,3,4,5,0,0,0], ic(correct_shift_zeros([1,2,3,0,0,4,0,5]))
assert correct_shift_zeros([0,0,0,1,2,5]) == [1,2,5,0,0,0], ic(correct_shift_zeros([0,0,0,1,2,5]))
assert correct_shift_zeros([0,0,0,0,0,1]) == [1,0,0,0,0,0], ic(correct_shift_zeros([0,0,0,0,0,1]))
assert correct_shift_zeros([0,1,2,3,4,0]) == [1,2,3,4,0,0], ic(correct_shift_zeros([0,1,2,3,4,0]))