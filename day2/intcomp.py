def int_comp(code):
    pointer = 0
    opcode = code[pointer]
    while opcode != 99:
        if opcode == 1:
            code[code[pointer + 3]] = code[code[pointer + 1]] + code[code[pointer + 2]]
        elif opcode == 2:
            code[code[pointer + 3]] = code[code[pointer + 1]] * code[code[pointer + 2]]
        pointer += 4
        opcode = code[pointer]

    return code


if __name__ == "__main__":
    with open('input2.txt') as f:
        prog = f.read().split(',')
        prog = [int(x) for x in prog]

    prog[1] = 12
    prog[2] = 2
    new_prog = int_comp(prog)
    print(new_prog)
