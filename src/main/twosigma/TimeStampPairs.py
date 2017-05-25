import threading


class Stream:
    def __init__(self, nums):
        self.nums = nums

    def getNext(self):
        return self.nums.pop()


class Calculator(object):
    def __init__(self):
        self.res = []
        self.q1 = []
        self.q2 = []

    def calculatePairs(self, value):
        self.q1.append(value)
        print self.q1
        print self.q2
        while self.q2 and value - self.q2[0] >= 1:
            self.q2.pop(0)
        for num in self.q2:
            if abs(num - value) < 1:
                self.res.append((value, num))

calculator = Calculator()
threadLock = threading.Lock()
def Iterator1(s):
    while True:
        try:
            value = s.getNext()
            threadLock.acquire()
            calculator.calculatePairs(value)
            threadLock.release()
        except:
            break

def Iterator2(s):
    while True:
        try:
            value = s.getNext()
            threadLock.acquire()
            calculator.calculatePairs(value)
            threadLock.release()
        except:
            break

if __name__ == '__main__':
    s1 = Stream([0.2, 1.4, 3.0])
    s2 = Stream([2.0, 2.1, 4.5])

    thread1 = threading.Thread(target=Iterator1, args=(s1,))
    thread1.setDaemon(True)

    thread2 = threading.Thread(target=Iterator2, args=(s2,))
    thread2.setDaemon(True)
    thread2.start()
    thread1.start()

    print calculator.res

