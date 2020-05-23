class Log(object):
    def __init__(self, log):
        self.log = log
        tokens = log.split(' ')
        self.identifer = tokens[0]
        self.letters = ' '.join(tokens[1:])


def reorder_logs(logs):
    letter_logs = []
    digit_logs = []

    for log in logs:
        token = log.split(' ')
        if token[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(Log(log))

    def compare(x, y):
        x_letter = x.letters
        y_letter = y.letters
        if x_letter <= y_letter:
            return -1
        if x.identifer == y.identifer:
            return 0
        else:
            return x.identifer < y.identifer

    letter_logs = sorted(letter_logs, cmp=compare)
    letter_logs = [x.log for x in letter_logs]
    return letter_logs + digit_logs


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    print reorder_logs(logs)
