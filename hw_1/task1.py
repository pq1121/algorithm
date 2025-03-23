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