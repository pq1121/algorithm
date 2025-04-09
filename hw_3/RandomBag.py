from random import randint

def malloc(size):
    return [None] * size


class RandomBag:


    def __init__(self, size=1):
        self.__size = size
        self.__array = malloc(self.__size)
        self.__count = 0


    def __str__(self):
        return f"{self.__array[:self.__count]}"


    def get_size(self):
        return self.__size


    def get_count(self):
        return self.__count


    def check_count(self):
        if self.__count == 0: raise ValueError("Мешок пуст")


    def new_size(self):
        self.__size *= 2
        new_array = malloc(self.__size)

        for i in range(self.__count):
            new_array[i] = self.__array[i]
        self.__array = new_array


    def check_size(self):
        pass


    def add(self, value):

        if self.__size == self.__count: self.new_size()

        self.__array[self.__count] = value
        self.__count += 1


    def count_item(self, value):
        self.check_count()
        count = 0

        for i in range(self.__count):

            if self.__array[i] == value:
                count += 1
        return count


    def get_random(self):
        self.check_count()
        index = randint(0,self.__count - 1)
        return self.__array[index]


    def contains(self, value):
        self.check_count()
        contain = False

        if value in self.__array:
            contain = True
        return contain


    def remove_random(self):
        self.check_count()
        index = randint(0,self.__count - 1)
        temp = self.__array[index]
        self.__array[index] = self.__array[self.__count-1]
        self.__count -= 1
        return temp


    def replace_random(self, value):
        self.check_count()
        index = randint(0,self.__count - 1)
        temp = self.__array[index]
        self.__array[index] = value
        return temp


    def remove_all(self, value):
        self.check_count()
        count = 0

        for i in range(self.__count):

            if self.__array[i] == value:
                self.__array[i] = None
                count += 1

        for i in range(1, self.__count):
            temp = self.__array[i]
            j = i

            while j > 0 and self.__array[j - 1] is None:
                self.__array[j] = self.__array[j - 1]
                j -= 1
            self.__array[j] = temp
        self.__count -= count