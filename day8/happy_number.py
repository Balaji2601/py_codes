def square_of_num(n):
    sum_ = 0
    while n > 0:
        sum_ += (n % 10) ** 2
        n = n // 10
    return sum_


def happy(n):
    s = set()
    while n != 1:
        n = square_of_num(n)
        # print(n)
        if n in s:
            return False
        s.add(n)
    return True


if __name__ == "__main__":
    n = 20
    out = happy(n)
    print(out)
