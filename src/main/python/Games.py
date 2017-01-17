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

        # one of the move is win, i can win, otherwise, lost.
        return move_one or move_two or move_three


def BullsAndCowsII(secret, guess):
    # only applies when secret and guess are all numbers
    # if could be alphabetical, we should allocate 26 size or 52 size depends on input.
    bCount = 0
    cCount = 0
    secretAppears = [0 for i in range(10)]
    guessAppears = [0 for i in range(10)]
    i = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            bCount += 1
        else:
            secretAppears[int(secret[i])] += 1
            guessAppears[int(guess[i])] += 1
        i += 1

    for i in range(10):
        cCount = cCount + min(secretAppears[i], guessAppears[i])

    return str(bCount) + 'A' + str(cCount) + 'B'


def BullsAndCows(secret, guess):
    aCount = 0
    bCount = 0
    potentialCow = []
    cowDict = dict()
    i = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            aCount += 1
        else:

            # it's in bull dict and also never get visited before
            if cowDict.has_key(guess[i]):
                bCount += 1
                count = cowDict.get(guess[i])
                if count >= 1:
                    cowDict[guess[i]] = count - 1
                else:
                    cowDict.pop(guess[i])
            else:
                potentialCow.append(i)

            if cowDict.has_key(secret[i]):
                # no matter what, secret key needs to in bullDict
                count = cowDict.get(secret[i])
                cowDict[secret[i]] = count + 1
            else:
                cowDict.setdefault(secret[i], 0)
        i += 1
    for p in potentialCow:
        if cowDict.has_key(guess[p]):
            bCount += 1
            count = cowDict.get(guess[p])
            if count >= 1:
                cowDict[guess[p]] = count - 1
            else:
                cowDict.pop(guess[p])
    return str(aCount) + 'A' + str(bCount) + 'B'


if __name__ == '__main__':
    games = Games()

    print games.canWinNim(1348820612)

    print BullsAndCows('1807', '7810')
    print BullsAndCowsII('1807', '7810')
    print BullsAndCows('1', '0')
    print BullsAndCowsII('1', '0')
    print BullsAndCows('1234', '0111')
    print BullsAndCowsII('1234', '0111')
    print BullsAndCows('1122', '2211')
    print BullsAndCowsII('1122', '2211')
