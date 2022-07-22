# 1. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def getting_list_of_coefficients(new_string):
    new_string = new_string.replace(" = 0", "")
    new_string = new_string.replace(" ", "")
    # print(new_string)
    list_of_coefficients = [0, 0, 0]
    num = ''
    i0 = new_string.find('*x²')
    for i in range(i0 - 1, -1, -1):
        if new_string[i].isdigit() == True or new_string[i] == '-':
            num = new_string[i] + num
    list_of_coefficients[0] = int(num)
    num = ''
    i1 = new_string.find('*x', i0 + 2)
    for i in range(i1 - 1, i0 + 2, -1):
        if new_string[i].isdigit() == True or new_string[i] == '-':
            num = new_string[i] + num
    list_of_coefficients[1] = int(num)
    num = ''
    for i in range(len(new_string) - 1, i1 + 1, -1):
        if new_string[i].isdigit() == True or new_string[i] == '-':
            num = new_string[i] + num
    list_of_coefficients[2] = int(num)
    return list_of_coefficients

def sum_of_polynomials(list1, list2):
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list


with open('file1.txt', 'r', encoding='utf-8') as f1:
    s1 = f1.readline()

with open('file2.txt', 'r', encoding='utf-8') as f2:
    s2 = f2.readline()

print(f'Первый полином: {s1}')
print(f'Второй полином: {s2}')

l1 = getting_list_of_coefficients(s1)
l2 = getting_list_of_coefficients(s2)

print(f'Коэффициенты первого полинома {l1}')
print(f'Коэффициенты второго полинома {l2}')

sum = sum_of_polynomials(l1, l2)
print(f'Список сумм коэффициентов {sum}')

sum_pol = f'{sum[0]}*x² + {sum[1]}*x + {sum[2]} = 0'
print(f'Сумма: {sum_pol}')

with open('file_sum.txt', 'w', encoding='utf-8') as fsum:
    fsum.write(sum_pol)