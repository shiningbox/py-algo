
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def length(matrix, i, j):
    return matrix[i + 1][j + 1]


def update_length(matrix, i, j, value):
    matrix[i + 1][j + 1] = value


def create_matrix(row_size, col_size):
    # The first row and column are zero L[-1, j] = 0, L[i, -1] = 0
    # Initial the first column to be zero L[-1, j] = 0
    lcs_matrix = [[None for i in range(col_size)] for j in range(row_size)]
    for i in range(row_size):
        lcs_matrix[i][0] = 0
    for j in range(col_size):
        lcs_matrix[0][j] = 0
    return lcs_matrix


class LCS:

    def __init__(self):
        pass

    @staticmethod
    def max(a, b):
        if a >= b:
            return a
        else:
            return b

    def find(self, seq1, seq2) -> int:
        x_len = len(seq1)
        y_len = len(seq2)
        lcs_matrix = create_matrix(x_len + 1, y_len + 1)
        for i in range(x_len):
            for j in range(y_len):
                # if xi = yj, xi and yj must be in the lcs, so L(i-1, j-1) + 1
                if seq1[i] == seq2[j]:
                    # L(i, j) = L(i-1, j-1) + 1
                    new_value = length(lcs_matrix, i - 1, j - 1) + 1
                else:
                    # if xi != yj
                    # L(i, j) = max(L(i, j-1), L(i-1, j))
                    new_value = max(length(lcs_matrix, i - 1, j), length(lcs_matrix, i, j - 1))
                update_length(lcs_matrix, i, j, new_value)
        return lcs_matrix


y = ['C', 'G', 'A', 'T', 'A', 'A', 'T', 'T', 'G', 'A', 'G', 'A']
x = ['G', 'T', 'T', 'C', 'C', 'T', 'A', 'A', 'T', 'A']
lcs = LCS()
lcs_result = lcs.find(x, y)
print_matrix(lcs_result)
