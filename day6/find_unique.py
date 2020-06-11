def find_unique(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] in d:
            v = d[arr[i]]
            d[arr[i]] = v + 1
        else:
            d[arr[i]] = 1
    for k, v in d.items():
        if v == 1:
            return k


if __name__ == "__main__":
    inp = [1, 2, 3, 4, 3, 2, 1]
    out = find_unique(inp)
    print(out)

