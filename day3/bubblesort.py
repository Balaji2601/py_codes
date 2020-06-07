def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr


if __name__ == "__main__":
    inp = [45, 62, 6, 7, 10, 145]
    test = list(inp)
    test.sort()
    out = bubble_sort(inp)
    print(out == test)
    print(test)
    print(inp)
