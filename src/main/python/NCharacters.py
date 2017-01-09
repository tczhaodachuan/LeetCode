class Reader4(object):
    def __init__(self, count):
        self.content = range(count)
        self.count = 0

    def read4(self, buff):
        left = self.count
        for i in range(min(4, len(self.content) - left)):
            buff.append(self.content[self.count])
            self.count += 1
        return min(4, len(self.content) - left)


class Reader(object):
    def __init__(self):
        self.buffer = []
        self.endOfFile = False

    def read(self, buff, n, reader4):
        if n == 0:
            return n
        i = 0
        readSize = 0
        while i <= n / 4:
            readBuffSize = reader4.read4(buff)
            if readBuffSize == 0:
                return readSize
            if readBuffSize < 4:
                return min(n, readSize + readBuffSize)
            readSize += readBuffSize
            i += 1
        return min(n, readSize)

    def readII(self, buff, n, reader4):
        if n == 0:
            return 0
        total = 0
        # if buffer size is less than what we need, and it's not EOF yet
        while len(self.buffer) < n and not self.endOfFile:
            r = reader4.read4(self.buffer)
            if r < 4:
                self.endOfFile = True
        for i in range(min(len(self.buffer), n)):
            buff.append(self.buffer.pop(0))
            total += 1
        return total


if __name__ == '__main__':
    reader4 = Reader4(8)
    reader = Reader()
    buff = []

    print reader.readII(buff, 1, reader4)
    print buff
    print reader.readII(buff, 2, reader4)
    print buff
    print reader.readII(buff, 6, reader4)
    print buff
