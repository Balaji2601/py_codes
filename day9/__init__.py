def sum_of(arr, first_el):
    new = [first_el]
    el = 0
    for i in range(1, len(arr)):
        el = arr[i] + new[i - 1]
        new.append(el)
    return new


if __name__ == "__main__":
    inp = [1, 2, 3, 4]
    first_el = inp[0]
    out = sum_of(inp, first_el)
    print(out)
