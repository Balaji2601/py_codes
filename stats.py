# finding mean,mode,median

import statistics as st


def mean_of_data(inp):
    count = 0
    sum = 0
    for i in inp:
        count += 1
        sum += i
    mn = sum / count
    return mn


def median_of_data(inp):
    a = len(inp)
    inp.sort()
    if a % 2 == 0:
        mdn = (inp[(a // 2) - 1] + inp[a // 2]) / 2
    else:
        mdn = inp[a // 2]
    return mdn


def stats(inp):
    mn = mean_of_data(inp)
    mdn = median_of_data(inp)
    md = max(set(inp), key=inp.count)
    return mn, mdn, md


if __name__ == '__main__':
    inp = [2, 3, 4, 1, 2, 5, 4, 2, 7]
    mn, mdn, md = stats(inp)
    print(st.mean(inp), st.median(inp), st.mode(inp))
    print(mn, mdn, md)
