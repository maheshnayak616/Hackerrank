__author__ = 'mahesh.nayak'


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    @property
    def data(self): self.__data

    @property
    def next(self): self.__next

