from time import sleep
class Foo(object):
    def __init__(self):
        self.counter = 0


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.counter = 1



    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() outputs "second". Do not change or remove this line.
        while self.counter != 1:
            sleep(0.01)
        printSecond()
        self.counter = 2


    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        # printThird() outputs "third". Do not change or remove this line.
        while self.counter != 2:
            sleep(0.01)
        printThird()
