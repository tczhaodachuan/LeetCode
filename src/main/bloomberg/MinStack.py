class MinStack(object):
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, n):
        self.main_stack.append(n)
        if len(self.min_stack) == 0 or self.min_stack[-1] > n:
            self.min_stack.append(n)

    def get_min(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]

        else:
            return

    def top(self):
        if len(self.main_stack) == 0:
            return

        return self.main_stack[-1]

    def pop(self):
        if len(self.main_stack) == 0:
            return

        top = self.main_stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return top


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(4)
    minStack.push(70)
    minStack.push(2)
    minStack.push(100)

    print minStack.get_min()
    minStack.pop()
    print minStack.get_min()
    minStack.pop()
    print minStack.get_min()
