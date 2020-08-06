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


if __name__ == '__main__':
    inp = "sAI_Balaji kothINti-IIT"
    out = capitalize_one(inp, [' ', '_'])
    print(out)
    assert capitalize(inp, [' ', '_']) == "Sai Balaji Kothinti-iit"
    assert capitalize_one(inp, [' ', '_', '-']) == "Sai Balaji Kothinti Iit"


