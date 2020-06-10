def find_unique(arr):
    for i in range(len(arr)):
        duplicate_found = False
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                duplicate_found = True
                break
        if not duplicate_found:
            return arr[i]


def find_unique_linear(arr):
    ans = 0
    for i in arr:
        ans = i ^ ans
    return ans


if __name__ == "__main__":
    inp = [1, 2, 1, 3, 5, 8, 8, 7, 7, 5, 3]
    out_xor = find_unique_linear(inp)
    out = find_unique(inp)
    print(out)
    print(out_xor)
