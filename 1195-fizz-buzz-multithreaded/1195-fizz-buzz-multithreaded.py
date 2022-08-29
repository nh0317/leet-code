from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock4 = Lock()
        
        self.lock3.acquire()
        self.lock2.acquire()
        self.lock4.acquire()
        
    def release_lock(self, i):
        if i % 3 == 0 and i % 5 == 0:
            self.lock2.release()
        elif i % 3 != 0 and i % 5 == 0:
            self.lock3.release()
        elif i % 3 == 0 and i % 5 != 0:
            self.lock4.release()
        else:
            self.lock1.release()
            
            
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 != 0:
                self.lock4.acquire()
                printFizz()
                self.release_lock(i+1)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
             if i % 3 != 0 and i % 5 == 0:
                self.lock3.acquire()
                printBuzz()
                self.release_lock(i+1)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.lock2.acquire()
                printFizzBuzz()
                self.release_lock(i+1)
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 != 0 and i % 5 != 0:
                self.lock1.acquire()
                printNumber(i)
                self.release_lock(i+1)

        