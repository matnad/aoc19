from day2.intcomp import int_comp

if __name__ == "__main__":
    with open('input2.txt') as f:
        prog = f.read().split(',')

    prog = [int(x) for x in prog]

    n = -1
    v = 0
    out = prog[0]
    target = 19690720

    while out != target:
        if n == 99:
            v += 1
            n = 0
        else:
            n += 1
        code = prog[:]
        code[1] = n
        code[2] = v
        code = int_comp(code)
        out = code[0]

    print(100 * n + v)
