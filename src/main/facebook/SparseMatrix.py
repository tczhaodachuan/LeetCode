def sparse_matrix(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0

    def compress(matrix):
        result = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    result.setdefault(i, {})[j] = matrix[i][j]
        return result

    compress_A = compress(A)
    compress_B = compress(B)
    m = len(A)
    n = len(B[0])

    result_matrix = [[0 for _ in range(n)] for _ in range(m)]

    for i in compress_A:
        for k in compress_A[i]:
            for j in compress_B.get(k, {}):
                result_matrix[i][j] += compress_A[i][k] * compress_B[k][j]

    return result_matrix


def vector_product(v1, v2):
    i, j = 0, 0
    result = 0
    while i < len(v1) and j < len(v2):
        x1, y1 = v1[i]
        x2, y2 = v2[j]
        if x1 == x2:
            i += 1
            j += 1
            result += y1 * y2
        elif x1 < x2:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    print sparse_matrix([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
    print sparse_matrix([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 20, 0], [11, 0, 1]])

    print vector_product([(1, 1), (2, 2), (8, 5), (9, 6)], [(1, 1), (2, 2), (8, 5)])
