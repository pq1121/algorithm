# Task 1
def factorial(num:int):

    if not isinstance(num, int): raise TypeError("Число должно быть целым")

    if num < 0 or num > 20: raise ValueError("Число должно быть больше 0 и меньше 20")

    if num == 0 or num == 1:
        return 1
    else:
        factorial = 1

        for number in range(2, num + 1):
            factorial *= number
        return factorial

# Task 2
def fibonacci(num:int) -> list:

    if not isinstance(num, int): raise TypeError("Число должно быть целым")

    if num < 0: raise ValueError("Число должно быть больше 0")

    if num == 0: return [0]

    fib_lst = [0,1]

    if num != 1:

        for i in range (1,num):
            new_num = fib_lst[i-1] + fib_lst[i]
            fib_lst.append(new_num)
    return fib_lst