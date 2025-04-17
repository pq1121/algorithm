from datetime import datetime


class ZootopiaTask:

    def __init__(self, description: str, due_date: datetime):
        self.__description = description
        self.__due_date = due_date


class Node:

    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class ZootopiaTasksStack:

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, task: ZootopiaTask):
        self.__top = Node(task, self.__top)
        self.__size += 1

    def peek(self):

        if not self.is_empty():
            return self.__top.value

    def count(self): return self.__size

    def pop(self):

        if not self.is_empty():
            temp = self.__top.value
            self.__top = self.__top.prev
            self.__size -= 1
            return temp

    def is_empty(self):
        return self.__size == 0