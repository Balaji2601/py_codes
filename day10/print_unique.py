def to_tuple(inp):
    m = {}
    for i in inp:
        if i in m:
            v = m[i]
            m[i] = v + 1
        else:
            m[i] = 1
    s = sorted(m.items(), key=lambda k: k[1])
    # ans = []
    # for i in s:
    #     ans.append([i[0], i[1]])
    ans = [[i[0], i[1]] for i in s]
    return ans


def remove_min_unique(inp, k):
    updated_list = to_tuple(inp)
    rem = k
    if k >= len(inp):
        return 0
    while rem > 0:
        el = updated_list[0]
        if el[1] > rem:
            el[1] -= rem
            rem = 0
        else:
            rem = rem - el[1]
            updated_list.pop(0)
    return len(updated_list)


if __name__ == "__main__":
    inp = "abcbbc"
    k = 3
    out = remove_min_unique(inp, k)
    print(out)
