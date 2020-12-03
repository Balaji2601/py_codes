# Learning's : Split, Replace, Join, capitalize | map | assert


def capitalize(inp, delimeters):
    for i in delimeters:
        inp = inp.replace(i, ' ')
    arr = inp.split()
    out = []
    for i in arr:
        out.append(i.capitalize())
    return ' '.join(out)


def capitalize_one(inp, delimeters):
    for i in delimeters:
        inp = inp.replace(i, ' ')
    return ' '.join(map(lambda x: x.capitalize(), inp.split()))


def f():
    a = """
2.7-2.8
2.9-3.0
3.1-3.2
3.3-3.4
3.5-3.6
3.7-3.8
3.9-4.0
4.1-4.2
4.3-4.4
4.5-4.6
4.7-4.8
4.9-5.0
5.1-5.2
5.3-5.4
5.5-5.6
5.7-5.8"""


if __name__ == '__main__':
    inp = "sAI_Balaji kothINti-IIT"
    out = capitalize_one(inp, [' ', '_'])
    print(out)
    assert capitalize(inp, [' ', '_']) == "Sai Balaji Kothinti-iit"
    assert capitalize_one(inp, [' ', '_', '-']) == "Sai Balaji Kothinti Iit"
