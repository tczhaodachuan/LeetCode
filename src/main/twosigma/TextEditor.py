from array import array


class TextEditor(object):
    def __init__(self):
        # front stack
        self._f_stack = []
        # tail stack
        self._t_stack = []

    def insert(self, position, character):
        if position <= len(self._f_stack):
            # insert inside the front stack
            while len(self._f_stack) > position:
                last_char = self._f_stack.pop()
                self._t_stack.insert(0, last_char)
            self._f_stack.append(character)
        elif position <= len(self._f_stack) + len(self._t_stack):
            move_length = position - len(self._f_stack)
            count = 0
            while len(self._t_stack) > 0 and count < move_length:
                first_char = self._t_stack.pop(0)
                self._f_stack.append(first_char)
            self._t_stack.insert(0, character)

    def delete(self, p1, p2):
        if p2 <= len(self._f_stack):
            del self._f_stack[p1:p2]
        elif p1 == len(self._f_stack):
            del self._f_stack[p1]
            del self._t_stack[0:p2]
        else:
            start = p1 - len(self._f_stack)
            end = p2 - len(self._f_stack)
            if end > len(self._t_stack):
                del self._t_stack[start:len(self._t_stack)]
            else:
                del self._t_stack[start:end]


    def display(self):
        content = ''
        for c in self._f_stack:
            content = content + c

        for c in self._t_stack:
            content = content + c
        print content

if __name__ == '__main__':
    textEditor = TextEditor()
    textEditor.insert(0, 'h')
    textEditor.display()
    textEditor.insert(1, 'o')
    textEditor.display()
    textEditor.insert(1, 'e')
    textEditor.display()
    textEditor.insert(2, 'l')
    textEditor.display()

    textEditor.insert(3, 'l')
    textEditor.display()

    textEditor.insert(5, ' ')
    textEditor.display()

    textEditor.insert(6, 'w')
    textEditor.display()
    textEditor.insert(7, 'o')
    textEditor.display()
    textEditor.insert(8, 'r')
    textEditor.display()
    textEditor.insert(9, 'd')
    textEditor.display()
    textEditor.insert(9, 'l')
    textEditor.display()

    print textEditor._f_stack
    textEditor.delete(9,10)
    textEditor.display()
