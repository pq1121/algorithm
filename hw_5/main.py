def malloc(size):
    return [[] for i in range(size)]


def s_hash(key):
    return len(key)


class HashTableNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, size=10):
        self.__memory = malloc(size)
        self.__size = size
        self.__count = 0


    def __repr__(self):
        return str([[node.value for node in self.__memory[i]] for i in range(self.__size)])


    def get_count(self): return self.__count


    def get_size(self): return self.__size


    def get(self, key):
        index = self.__calculate_index(key)

        for node in self.__memory[index]:

            if node.key == key:
                return node.value
        return None


    def contains_key(self, key):
        return self.get(key) is not None

    def contains_value(self, key):
        return self.get(key)

    def __procent_is_empty(self):
        return self.__memory.count([])/self.__size


    def __checking_fulled(self):

        if self.__procent_is_empty() <= 0.25:
            new_size = self.__size * 2
            self.__rehash(new_size)


    def __rehash(self, new_size):
        new_memory = malloc(new_size)

        for i in range(self.__size):
            new_memory[i] = self.__memory[i]
        self.__size = new_size
        self.__memory = new_memory


    def __calculate_index(self, key):
        return s_hash(key) % self.__size


    def set(self, key, value):

        self.__checking_fulled()
        index = self.__calculate_index(key)

        if len(self.__memory[index]) == 0:
            self.__memory[index].append(HashTableNode(key, value))
            self.__count += 1
        else:
            found_index = -1

            for i in range(len(self.__memory[index])):

                if self.__memory[index][i].key == key:
                    found_index = i

            if found_index == -1:
                self.__memory[index].append(HashTableNode(key, value))
                self.__count += 1
            else:
                self.__memory[index][found_index].value = value


    def remove(self, key):
        index = self.__calculate_index(key)

        for i in range(len(self.__memory[index])):

            if self.__memory[index][i].key == key:
                temp = self.__memory[index].pop(i)
                self.__count -= 1
                return temp.value
        return None