def malloc(size):
    return [None] * size


class List:

    def __init__(self, size=1):
        self.__size = size
        self.__memory = [None] * size
        self.__count = 0


    def check_index(self, index):
        if index > self.__count or index < 0: raise ValueError("Индекс указан не верно")


    def new_size(self):
        self.__size = self.__size + (self.__size // 2 + 1)
        new_memory = malloc(self.__size)

        for i in range(self.__count):
            new_memory[i] = self.__memory[i]
        self.__memory = new_memory


    def add(self, value):

        if self.__size == self.__count:
            self.new_size()
        self.__memory[self.__count] = value
        self.__count += 1


    def insert(self, index, value):
        self.check_index(index)

        if self.__size == self.__count:
            self.new_size()
        i = self.__count

        while i > index:
            self.__memory[i] = self.__memory[i-1]
            i -= 1
        self.__memory[index] = value
        self.__count += 1


    def remove(self, value):
        target_index = -1

        if self.__size == self.__count:
            self.new_size()

        for i in range(self.__count):

            if self.__memory[i] == value:
                target_index = i
                break

        if target_index == -1: raise ValueError("Элемент не найдет")

        for i in range(target_index,self.__count):
            self.__memory[i] = self.__memory[i+1]
        self.__count -= 1


    def count(self, value):
        count = 0

        for i in range(self.__count):

            if self.__memory[i] == value:
                count += 1
        return count


    def find(self, value):

        for i in range(self.__count):

            if self.__memory[i] == value:
                return i


    def pop(self, index):
        self.check_index(index)
        value_index = self.__memory[index]

        if self.__size == self.__count:
            self.new_size()

        for i in range(index,self.__count):
            self.__memory[i] = self.__memory[i+1]
        self.__count -= 1
        return value_index


    def add_front(self, value):
        self.insert(0, value)

    def __str__(self):
        return f"{self.__memory}\nколичество: {self.__count}"