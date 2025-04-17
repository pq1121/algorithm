from datetime import datetime


class HogwartsClass:

    def __init__(self, description: str, instructor: str, start_time: datetime):
        self.description = description
        self.instructor = instructor
        self.start_time = start_time


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class HogwartsSchedule:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__target = None

    def add(self, clas: HogwartsClass):
        new_node = Node(clas)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            new_node.next = self.__head
            self.__target = self.__head
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__tail.next = self.__head

        self.__size += 1

    def get_current(self):

        if not self.is_empty():
            return self.__target.value.description

    def next(self):

        if not self.is_empty():

                self.__target = self.__target.next
                return self.__target.value.description

    def count(self): return self.__size

    def remove_current(self):
        if not self.is_empty():
            current_node = self.__head
            temp_value = self.__target.value.description

            while  current_node.next != self.__target:
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.__target = current_node.next
            self.__size -= 1
            return f"{temp_value} удалили из списка"

    def is_empty(self):
        return self.__size == 0