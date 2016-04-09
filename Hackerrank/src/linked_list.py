class node:
    def __init__(self):
        self.__next = None
        self.__data = None

    @property
    def next(self):
        return self.__next

    @property
    def data(self):
        return self.data

root = node()
root.data = 1
root.next = node()
root.next.data = 2
root.next.next = node()
root.next.next.data = 3
root.next.next.next = node()
root.next.next.next.data = 4
root.next.next.next.next = node()
root.next.next.next.next.data = 5

test = 3
prev = root
curr = root.next

if prev.data == 3:
    root = curr
else:
    while curr is not None and prev is not None:
        if curr.data == test:
            prev.next = curr.next
            curr = None
            break
        prev = curr
        curr = curr.next
n = root
while n is not None:
    print n.data
    n = n.next
