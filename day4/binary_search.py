def binary_search(arr, n):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if n == arr[m]:
            return True
        elif n > arr[m]:
            l = m+1
        else:
            r = m-1
    return False


if __name__ == "__main__":
    n = 10
    arr = [1, 3, 7, 11, 17, 25, 40]
    out = binary_search(arr, n)
    print(out)
