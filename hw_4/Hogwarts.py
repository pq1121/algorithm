from datetime import datetime


class HogwartsEvent:

    def __init__(self, description: str, event_date: datetime):
        self.__description = description
        self.__event_date = event_date


class Node:

    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class HogwartsEventQueue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def enqueue(self, event: HogwartsEvent):
        new_node = Node(event)

        if self.is_empty():
            self.__head = new_node

        else:
            self.__tail.prev = new_node
        self.__tail = new_node
        self.__size += 1

    def dequeue(self):

        if not self.is_empty():
            temp = self.__head.value
            self.__head = self.__head.prev
            self.__size -= 1
            return temp

    def peek(self):

        if not self.is_empty():
            return self.__head.value

    def is_empty(self):
        return self.__size == 0