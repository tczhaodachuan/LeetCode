class Polish(object):
    def __init__(self, polish_array):
        self.polish_array = polish_array
        self.operators = ['+', '-', '*', '/']

    def calculate(self):
        self.stack = []
        for polish in self.polish_array:
            if polish in self.operators:
                num1 = self.stack.pop()
                num2 = self.stack.pop()
                if polish == '+':
                    self.stack.append(num1 + num2)
                elif polish == '-':
                    self.stack.append(num2 - num1)
                elif polish == '*':
                    self.stack.append(num1 * num2)
                elif polish == '/':
                    self.stack.append(num2 / num1)
            else:
                self.stack.append(int(polish))
        return self.stack.pop()


if __name__ == '__main__':
    inputList = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    polish = Polish(inputList)
    print polish.calculate()
    inputList = ['10', '3', '+', '7', '-']
    polish = Polish(inputList)
    print polish.calculate()
