def shuffle(arr):
    out = []
    n = len(arr) // 2
    for i in range(n):
        out.append(arr[i])
        out.append(arr[i + n])
    return out


if __name__ == "__main__":
    inp = [1, 3, 5, 2, 4, 6]
    shuffled_inp = shuffle(inp)
    print(shuffled_inp)
