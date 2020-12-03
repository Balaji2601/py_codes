def derive_operator(inp):
    if "+" in inp:
        return "+"
    elif  "-" in inp:
        return "-"
    elif  "/" in inp:
        return "/"
    elif  "*" in inp:
        return "*"
def return_integers(inp,oper):
    arr = inp.split(oper)
    return int(arr[0]),int(arr[1])
def exp(inp):
    inp = inp.replace(' ','')
    ope = derive_operator(inp)
    a,b = return_integers(inp,ope)
    if ope == "+":
        return a+b
    if ope == "-":
        return a-b
    if ope == "/":
        return a/b
    if ope == "*":
        return a*b

if __name__ == '__main__':
    inp = "   2/   100   "
    t = exp(inp)
    print(t)
