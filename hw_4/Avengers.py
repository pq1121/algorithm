class AvengersMission:

    def __init__(self, description: str, priority: int):
        self.description = description
        self.priority = priority


class Node:

    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class AvengersPriorityQueue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def enqueue(self, event: AvengersMission):
        new_node = Node(event)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:

            if self.__head.value.priority >= event.priority:
                temp = self.__head
                self.__head = new_node
                self.__head.prev = temp
            elif self.__tail.value.priority < event.priority:
                self.__tail.prev = new_node
                self.__tail = new_node
            else:
                temp = self.__head

                while temp.prev is not None and new_node.value.priority > temp.prev.value.priority:
                    temp = temp.prev
                buff = temp.prev
                temp.prev = new_node
                temp.prev.prev = buff

        self.__size += 1

    def dequeue(self):

        if not self.is_empty():
            temp = self.__head.value
            self.__head = self.__head.prev
            self.__size -= 1
            return temp

    def peek(self):

        if not self.is_empty():
            return self.__head.value.description

    def is_empty(self):
        return self.__size == 0