from time import perf_counter
from sys import getsizeof


def next_bigger_num(nums):
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            yield nums[i]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Option 1
start_1 = perf_counter()
result_1 = list(next_bigger_num(src))
exec_time_1 = perf_counter() - start_1
print(f'{result_1} Execution time: {exec_time_1}, memory: {getsizeof(result_1)}')

# Option 2
start_2 = perf_counter()
result_2 = list(src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
exec_time_2 = perf_counter() - start_2
print(f'{result_2} Execution time: {exec_time_2}, memory: {getsizeof(result_2)}')

# Option 3
start_3 = perf_counter()
result_3 = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
exec_time_3 = perf_counter() - start_3
print(f'{result_3} Execution time: {exec_time_3}, memory: {getsizeof(result_3)}')
