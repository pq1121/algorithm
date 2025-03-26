# Task 1
def max_in_range(arr, start, end):

    n = len(arr)
    if start < 0 or end < 0: raise ValueError("Индексы указаны не верно")
    if start > n or end > n: raise ValueError("Индексы указаны не верно")
    max_elem = arr[start]
    absolute_index = start
    relative_index = 0

    for i in range(start+1, end+1):

        if arr[i] > max_elem:
            max_elem = arr[i]
            absolute_index = i
            relative_index = i - start

    return max_elem, absolute_index, relative_index