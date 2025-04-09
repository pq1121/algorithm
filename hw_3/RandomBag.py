from random import randint

def malloc(size):
    return [None] * size


class RandomBag:

    def __init__(self, size=1):
        self.__size = size
        self.__array = malloc(self.__size)
        self.__count = 0

    def check_index(self, index):
        if index > self.__count or index < 0: raise ValueError("Индекс указан не верно")

    def new_size(self):
        new_array = malloc(self.__size * 2)

        for i in range(self.__count):
            new_array[i] = self.__array[i]
        self.__array = new_array

    def check_size(self):
        pass

    def add(self, value):
        pass