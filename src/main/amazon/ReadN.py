def read(buf, N):
    while len(buf) < N:
        read_cnt, temp_buf = read4()
        if read_cnt < 4:
            for ch in temp_buf:
                buf.append(ch)
            break
        if read_cnt == 4:
            for ch in temp_buf:
                buf.append(ch)


def read4():
    import random
    number = random.randint(0, 4)
    return number, ['a' * number]

if __name__ == '__main__':
    buf = []
    read(buf, 5)
    print buf