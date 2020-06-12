def is_symmetric(arr):
    if len(arr) != len(arr[0]):
        return False
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return False
    return True


if __name__ == "__main__":
    inp = [[0, 1, 2],
           [1, 2, 5],
           [2, 5, 0]]
    out = is_symmetric(inp)
    print(out)
