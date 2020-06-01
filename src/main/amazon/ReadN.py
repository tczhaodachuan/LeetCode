def read(buf, N):
    # either read N characters or reach the end of the file
    eof = False
    total = 0

    count = 0
    while total < N and not eof:
        read_cnt, temp_buf = read4(count)
        if read_cnt < 4:
            eof = True

        # the last batch, we may not need to read the full temp buff
        read_cnt = min(read_cnt, N - total)
        for i in range(read_cnt):
            buf[total + i] = temp_buf[i]
        total += read_cnt
        count += 1
    return total


class ReadN(object):
    def __init__(self):
        self.read_buffer = []
        # track where it was left in the last read
        self.offset = 0
        self.remaining_chars = 0

    def readII(self, buf, N):
        eof = False
        # local variable for the current read
        total_read = 0
        # this function could be called multiple times
        # the only difference compare with the above one is we need to store the state of the last read
        # read multiple times, could be the last read didn't finish all the characters in the buffer
        # so next time it reads, we release the chars left in the buffer
        while not eof and total_read < N:
            if self.remaining_chars == 0:
                self.remaining_chars, self.read_buffer = read4(5)
                if self.remaining_chars < 4:
                    eof = True
            # read remaining chars first if there are any
            demand_cnt = min(self.remaining_chars, N - total_read)
            for i in range(demand_cnt):
                buf[total_read + i] = self.read_buffer[self.offset + i]
            total_read += demand_cnt
            self.remaining_chars -= demand_cnt
            # buffer has 4 chars, but read 1 last time, the first read will reset offset to 0
            self.offset = (self.offset + demand_cnt) % 4
        return buf


def read4(count):
    if count < 4:
        return 4, 'zhad'
    else:
        return 2, 'zh'


if __name__ == '__main__':
    buf = [0] * 5
    read(buf, 5)
    print buf
