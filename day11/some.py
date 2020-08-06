def capitalize(inp, delimeters):
    for i in delimeters:
        inp = inp.replace(i,' ')
    arr = inp.split()
    out = []
    for i in arr:
        out.append(i.capitalize())
    return ' '.join(out)


if __name__ == '__main__':
    inp = "sAI_Balaji kothINti-IIT"
    out = capitalize(inp, [' ', '_'])
    print(out)
    assert capitalize(inp, [' ', '_']) == "Sai Balaji Kothinti-iit"
    assert capitalize(inp, [' ', '_', '-']) == "Sai Balaji Kothinti Iit"
