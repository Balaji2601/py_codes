def sum_of(arr, first_el):
    new = [first_el]
    el = 0
    for i in range(1, len(arr)):
        el = arr[i] + new[i - 1]
        new.append(el)
    return new


def reverse_sum_of(arr):
    last_el = arr[len(arr) - 1]
    new = [last_el]
    el = 0
    for i in range(len(arr) - 1, 0, -1):
        el = arr[i - 1] + new[0]
        new.insert(0, el)
    return new


if __name__ == "__main__":
    inp = [1, 2, 3, 4]
    first_el = inp[0]
    out = sum_of(inp, first_el)
    out_of_reverse_sum = reverse_sum_of(inp)
    print(out)
    print(out_of_reverse_sum)
