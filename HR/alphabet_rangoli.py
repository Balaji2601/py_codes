# array reverse, indices slicing, string ascii, power of function
import string
from typing import List, Any

alphabet_string = string.ascii_lowercase
alphabet_list: List[Any] = list(alphabet_string)


def create_line(cur, n):
    line = ""
    for i in range(cur, n):
        line += alphabet_list[i]
        if alphabet_list[i] == alphabet_list[n - 1]:
            break
        else:
            line += "-"
    rev_line = line[::-1]
    line = rev_line + line[1:]

    line = cur * "--" + line + cur * "--"
    return line


def print_rangoli(n):
    lines = []
    for i in range(n):
        lines.append(create_line(i, n))
    rev_lines = lines[::-1]
    ans = rev_lines + lines[1:]
    for line in ans:
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
