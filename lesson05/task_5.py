from time import perf_counter


def get_non_repeat_nums(nums):
    repeat_nums = []
    non_repeat_nums = []
    for i in range(len(nums)):
        if nums[i] in non_repeat_nums:
            non_repeat_nums.remove(nums[i])
            repeat_nums.append(nums[i])
        elif nums[i] not in non_repeat_nums:
            non_repeat_nums.append(nums[i])
    return non_repeat_nums


def get_repeat_nums(nums):
    counter = {}
    for elem in nums:
        counter[elem] = counter.get(elem, 0) + 1
    rep_nums = {element: count for element, count in counter.items() if count > 1}.keys()
    return rep_nums


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Option 1
start_1 = perf_counter()
result_1 = get_non_repeat_nums(src)
exec_time_1 = perf_counter() - start_1
print(result_1, exec_time_1)

# Option 2
start_2 = perf_counter()
doubles = get_repeat_nums(src)
result_2 = [num for num in src if num not in doubles]
exec_time_2 = perf_counter() - start_2
print(result_2, exec_time_2)

