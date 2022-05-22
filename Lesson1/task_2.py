# function to get sum of all digits in number
def get_sum_of_digits(number):
    dig_sum = 0
    while number:
        dig_sum += number % 10
        number = number // 10
    return dig_sum


# function to get sum of numbers divisible by 7
def sum_num_divisible_7(numbers):
    total = 0
    for number in numbers:
        # check division by seven
        if get_sum_of_digits(number) % 7 == 0:
            total += number
    return total


# function to get sum of numbers divisible by 7 with additional 17
def sum_num_divisible_7_add_17(numbers):
    total = 0
    for number in numbers:
        # add 17
        number += 17
        # check division by seven
        if get_sum_of_digits(number) % 7 == 0:
            total += number
    return total


num_list_1 = []
# add numbers to list
for i in range(1000):
    if (i + 1) % 2 != 0:
        num_list_1.append((i + 1) ** 3)

num_list_2 = []
# add numbers to list 2
for num in num_list_1:
    num_list_2.append(num + 17)

total_1 = sum_num_divisible_7(num_list_1)
total_2 = sum_num_divisible_7(num_list_2)
total_3 = sum_num_divisible_7_add_17(num_list_1)

print(f'Список 1, состоящий из кубов нечётных чисел от 1 до 1000: {num_list_1}')
print(f'Сумма тех чисел из списка 1, сумма цифр которых делится нацело на 7: {total_1}')
print(f'Список 2, состоящий из кубов нечётных чисел от 1 до 1000, к которым прибавлено 17: {num_list_2}')
print(f'Сумма тех чисел из списка 2, сумма цифр которых делится нацело на 7: {total_2}')
print(f'Сумма чисел без создания дополнительного списка: {total_3}')