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

# Task 3
def  reverse_even_elements(arr: list[int]):

    if not isinstance(arr, list): raise TypeError()

    n = len(arr)
    index_temp_arr = []
    temp_arr = []

    for i in range(n):

        if arr[i] % 2 == 0:
            index_temp_arr.append(i)
            temp_arr.append(arr[i])
    temp_arr.reverse()

    for i in range(len(index_temp_arr)):
        arr[index_temp_arr[i]] = temp_arr[i]

    return arr

# Task 4
def inc_number(digits:list):

    inc = 0
    n = len(digits)

    if not isinstance(digits, list): raise TypeError

    for i in range(-1, -n-1, -1):

        if not isinstance(digits[i], int): raise TypeError()

        elif digits[i] > 9 or digits[i] <= 0: raise ValueError()

        elif inc == 0:
            digits[i] += 1
            inc = 1
            if digits[i] > 9:
                digits[i] = 0
                inc = 0
            if i == -n:
                digits.insert(0,1)

    return digits

# Task 7
def three_sum_unique(arr: list):

    if not isinstance(arr, list): raise TypeError
    temp_arr = []
    n = len(arr)

    if n < 3: raise ValueError()

    for i in range(n):

        for j in range(i+1, n):

            for k in range(j+1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    lst = [arr[i], arr[j], arr[k]]
                    if lst not in temp_arr:
                        temp_arr.append(lst)

    if temp_arr:
        return temp_arr