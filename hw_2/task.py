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

# Task 2
def rotate_and_reverse(arr: list, k: int):

    if not isinstance(k, int): raise TypeError()
    if k < 0: raise ValueError("Число должно быть больше либо равно нулю")
    n = len(arr)
    result_arr = []

    if k > n:
        k = k % n

    if n == k and k == 0:

        for i in range(n):
            result_arr.append(arr[i])

    else:

        for i in range(n-k, n, 1):
            result_arr.append(arr[i])

        for i in range(0, n-k, 1):
            result_arr.append(arr[i])

    return result_arr[::-1]