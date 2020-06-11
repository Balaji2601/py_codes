def numJewelsInStones(J, S):
    count = 0
    j = set()
    for e in J:
        j.add(e)
    for e in S:
        if e in j:
            count += 1
    return count


if __name__ == "__main__":
    J = "aA"
    S = "ssssaAAAAbBBBB"
    out = numJewelsInStones(J, S)
    print(out)
