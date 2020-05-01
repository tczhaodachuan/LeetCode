class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        self.sum_matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            row_total = 0
            for j in range(n):
                row_total += matrix[i][j]
                self.sum_matrix[i][j] = row_total

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        for row in range(row1, row2 + 1):
            if col1 == 0:
                result += self.sum_matrix[row][col2]
            else:
                result += self.sum_matrix[row][col2] - self.sum_matrix[row][col1 - 1]
        return result


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    num_matrix = NumMatrix(matrix)

    print num_matrix.sumRegion(2, 1, 4, 3)
