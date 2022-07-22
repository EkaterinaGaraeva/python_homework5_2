# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#
# Пример:
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

import random

# def find_sequence(list_of_numbers):
#     sequence = [list_of_numbers[0]]
#     for i in list_of_numbers:
#         if (i > max(sequence)):
#             sequence.append(i)
#     return sequence

def find_sequence2(list_of_numbers):
    index = random.randint(0, len(list_of_numbers) - 2)
    sequence = [list_of_numbers[index]]
    for i in range(index + 1, len(list_of_numbers)):
        if (list_of_numbers[i] > max(sequence)):
            sequence.append(list_of_numbers[i])
    return sequence


numbers = [1, 5, 2, 3, 4, 6, 1, 7]
numbers2 = [1, 5, 2, 3, 4, 1, 7]
# print(f'[1, 5, 2, 3, 4, 6, 1, 7] => {find_sequence(numbers)}')
# print(f'[1, 5, 2, 3, 4, 1, 7] => {find_sequence(numbers2)}')

print(f'[1, 5, 2, 3, 4, 6, 1, 7] => {find_sequence2(numbers)}')
print(f'[1, 5, 2, 3, 4, 1, 7] => {find_sequence2(numbers2)}')