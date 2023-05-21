# ДЗ на понедельник (Ivanov_Lesson_16.py) - скидывает на гитхаб
# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать,
# требуется только изменение переданного списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]


def modify_list(nums):
    i = 0
    while i < len(nums):
        if isinstance(nums[i], int) and nums[i] % 2 == 0:
            nums[i] //= 2
            i += 1
        else:
            del nums[i]


nums = [1, '2', 3, 4, 5, 6, 7, 8, 9, 10]
print(modify_list(nums))
print(nums)
modify_list(nums)
print(nums)
nums = [16, 5, 20, 1]
modify_list(nums)
print(nums)
modify_list(nums)
print(nums)
