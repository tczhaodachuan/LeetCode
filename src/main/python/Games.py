class Games(object):
    def canWinNim(self, n):
        matrix = dict()
        return self.play(n, True, matrix)

    def play(self, n, myStep, matrix):
        if n <= 3:
            if myStep:
                return True
            else:
                return False

        if n % 4 == 0:
            return False
        else:
            return True


        if matrix.has_key(n - 3):
            move_three = matrix.get(n - 3)
        else:
            move_three = self.play(n - 3, not myStep, matrix)
            matrix.setdefault(n - 3, move_three)

        if matrix.has_key(n - 2):
            move_two = matrix.get(n - 2)
        else:
            move_two = self.play(n - 2, not myStep, matrix)
            matrix.setdefault(n - 2, move_two)

        if matrix.has_key(n - 1):
            move_one = matrix.get(n - 1)
        else:
            move_one = self.play(n - 1, not myStep, matrix)
            matrix.setdefault(n - 1, move_one)



        return move_one or move_two or move_three


if __name__ == '__main__':
    games = Games()

    print games.canWinNim(1348820612)
