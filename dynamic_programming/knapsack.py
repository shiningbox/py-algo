def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def create_matrix(row_size, col_size):
    return [[0 for i in range(col_size + 1)] for j in range(row_size+1)]

def max(a, b):
    if a >= b:
        return a
    else:
        return b

class Knapsack:
    "For all possible w from 0 to W"
    "For each item with wk, k from 0 to n-1"
    "For each weight chunk wk to W"
    "If adding k will improve its weight quality (value)"
    "   B[k-1, w-wk] + bk > B[k-1, w]"
    "   Then include wk and update B[k, w]"
    "Else"
    "   Move to next w"

    "Keep the weight update history in a matrix"
    def __init__(self):
        pass

    def brute_force(self, weights, values, max_weight):
        max_value = 0
        weights_len = len(weights)
        # x mod 2
        # x/2 mod 2
        # x/4 mod 2
        # ...
        combinations = []
        max_combination = []

        for num in range(2 ** weights_len):
            binary = [0] * weights_len
            for i in range(weights_len):
                binary[i] = num % 2
                num = int(num/2)
            combinations.append(binary)

        # For each possible item combination
        for combination in combinations:
            weight_sum = 0
            value_sum = 0
            index = 0
            for value in combination:
                if value == 1:
                    weight_sum += weights[index]
                    value_sum += values[index]
                index += 1
            if weight_sum <= max_weight and value_sum >= max_value:
                max_value = value_sum
                max_combination = combination
        return max_value, max_combination

    def pack(self, weights, values, max_weight):
        weight_len = len(weights)
        value_matrix = create_matrix(weight_len, max_weight)

        # for each item k
        for k in range(0, weight_len):
            # for each wk to W
            w_k = weights[k]
            for w in range(0, max_weight + 1):
                old_value_w = value_matrix[k][w]
                if w >= w_k:
                    new_value_w = value_matrix[k][w - w_k] + values[k]
                    # Check if we can add item k
                    # only if adding k will increase the max value
                    if new_value_w > old_value_w:
                        value_matrix[k+1][w] = new_value_w
                    else:
                        value_matrix[k+1][w] = old_value_w
                else:
                    # if current weight can not hold the w_k
                    value_matrix[k+1][w] = old_value_w
        max_value = value_matrix[k][max_weight]
        print(max_value)
        w = max_weight
        # For each item k, check if it is added to the best subset of max_weight
        # If its max value was updated (via adding k), then k is added
        # e.g.,
        "0 0 0 0 0 0 0 0 0 0 0"
        "0 3 3 3 3 3 3 3 3 3 3"
        "0 3 3 3 3 3 5 5 5 5 5"
        "0 3 3 3 6 9 9 9 9 9 11"
        "0 3 3 4 7 9 9 10 13 13 13"
        "0 3 3 4 7 9 9 10 13 13 13"

        # weights = [1, 5, 4, 3, 6]
        # values = [3, 2, 6, 4, 5]

        # max_value = 13, max_weight = 10
        # row_index = 5, 4, 3, 2, 1, 0
        # row_index = 5,
        # if B[5][20] > B[4][20], 13=13 then item 4 was added before , else not
        # row_index = 4, if B[4][10] > B[3][10], 13>11.  Add 4-1
        # Check the rest values and weights, max_value - value[4-1] = 9, max_weight - weight[4-1] = 7
        # row_index = 3, if B[3][7] > B[2][7], 9 > 5. Add 3-1
        # Check the rest values and weights, max_value - value[3-1] = 3, max_weight - weights[3-1] = 3
        # row_index = 2, if B[2][3] > B[1][3], 3 = 3
        # row_index = 1, if B[1][3] > B[0][3], 3>0. Add 1-1

        for row_index in range(weight_len, 0, -1):
            item_index = row_index - 1
            if max_value <= 0:
                break
            # If the max value is the same with last item, then k is not added
            if max_value == value_matrix[item_index][w]:
                continue
            else:
                print(item_index)
                max_value = max_value - values[item_index]
                w = w - weights[item_index]

        return value_matrix


weights = [1, 5, 4, 3, 6]
values = [3, 2, 6, 4, 5]
max_weight = 10
knapsack = Knapsack()
max_value, max_combination = knapsack.brute_force(weights, values, max_weight)
print(f"max value {max_value}")
print(f"max combination {max_combination}")
value_matrix = knapsack.pack(weights, values, max_weight)
print_matrix(value_matrix)
