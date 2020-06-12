def column_sum(arr, index):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][index]
    return ans


def row_sum(arr, index):
    ans = 0
    for i in range(len(arr[0])):
        ans += arr[index][i]
    return ans


def sum_equal(arr):
    ans = []
    for i in range(len(arr)):
        rs = row_sum(arr, i)
        for index in range(len(arr[0])):
            if rs == column_sum(arr, index):
                ans.append((i, index))
    return ans


if __name__ == "__main__":
    inp = [[0, 1, 2], [1, 2, 5], [2, 1, 0]]
    out = sum_equal(inp)
    print(out)
