def f(inp):
    l, r, ans = 0, 0, 0
    sub = set()
    for i in range(len(inp)):
        c = inp[i]
        if c not in sub:
            sub.add(c)
            ans = max(ans, r - l + 1)
        else:
            while inp[l] != c:
                sub.remove(inp[l])
                l+=1
            l+=1
        r += 1
    return ans


if __name__ == "__main__":
    inp = "pwwkew"
    print(f(inp))
