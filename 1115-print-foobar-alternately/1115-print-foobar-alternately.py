from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = Lock()
        self.lock2 = Lock()
        
        self.lock1.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock2.acquire()
            printFoo()
            self.lock1.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock1.acquire()
            printBar()
            self.lock2.release()