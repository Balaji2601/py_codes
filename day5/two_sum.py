def two_sum(arr, n):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == n:
            return True
        elif arr[left] + arr[right] > n:
            right -= 1
        else:
            left += 1
    return False


if __name__ == "__main__":
    inp = [1, 2, 4, 6, 10, 15, 22, 37]
    n = 40
    out = two_sum(inp, n)
    print(out)
