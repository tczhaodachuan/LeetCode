class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        validated_rows = {}
        validated_cols = {}
        validated_cube = {}
        valid_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isdigit():
                    valid_set = valid_digits.copy()
                    if j not in validated_cols:
                        for k in range(len(board)):
                            if board[k][j].isdigit():
                                if board[k][j] in valid_set:
                                    valid_set.remove(board[k][j])
                                else:
                                    return False
                        validated_cols[j] = True

                    valid_set = valid_digits.copy()
                    if i not in validated_rows:
                        for k in range(len(board)):
                            if board[i][k].isdigit():
                                if board[i][k] in valid_set:
                                    valid_set.remove(board[i][k])
                                else:
                                    return False
                        validated_rows[i] = True

                    # validate the small cube
                    cube_row_start = i / 3 * 3
                    cube_col_start = j / 3 * 3
                    valid_set = valid_digits.copy()
                    if (cube_row_start, cube_col_start) not in validated_cube:
                        for m in range(cube_row_start, cube_row_start + 3):
                            for n in range(cube_col_start, cube_col_start + 3):
                                if board[m][n].isdigit():
                                    if board[m][n] in valid_set:
                                        valid_set.remove(board[m][n])
                                    else:
                                        return False
                    validated_cube[(cube_row_start, cube_col_start)] = True
        # print validated_rows
        # print validated_cols
        # print validated_cube
        return True


if __name__ == '__main__':
    s = Solution()
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print s.isValidSudoku(board1)

    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print s.isValidSudoku(board2)

    print 'board3'
    board3 = [[".", ".", ".", "9", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", "3", ".", ".", ".", ".", ".", "1"],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              ["1", ".", ".", ".", ".", ".", "3", ".", "."],
              [".", ".", ".", ".", "2", ".", "6", ".", "."],
              [".", "9", ".", ".", ".", ".", ".", "7", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              ["8", ".", ".", "8", ".", ".", ".", ".", "."]]
    print s.isValidSudoku(board3)
    print 'board4'
    board4 = [[".", ".", "5", ".", ".", ".", ".", ".", "."],
              ["1", ".", ".", "2", ".", ".", ".", ".", "."],
              [".", ".", "6", ".", ".", "3", ".", ".", "."],
              ["8", ".", ".", ".", ".", ".", ".", ".", "."],
              ["3", ".", "1", "5", "2", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "4", "."],
              [".", ".", "6", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "9", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    print s.isValidSudoku(board4)

    print 'board5'
    board5 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print s.isValidSudoku(board5)
