import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=7)
in1 = [int(x) for x in puzzle.input_data.split(',')]
print(in1)


def run(program, inp, pointer=0):
    num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3]
    i = pointer
    input_memory = 0
    out = 0
    while program[i] != 99:
        modes = [int(x) for x in f"{program[i]:0>5}"[:3]][::-1]
        instruction = int(f"{program[i]:0>5}"[3:])
        operands = [program[i + x + 1] if modes[x] else program[program[i + x + 1]] for x in
                    range(num_of_operands[instruction])]
        # print(modes, instruction, operands)
        if instruction == 1:
            program[program[i + 3]] = operands[0] + operands[1]
        elif instruction == 2:
            program[program[i + 3]] = operands[0] * operands[1]
        elif instruction == 3:
            program[program[i + 1]] = inp  # input_list[0] if input_memory == 0 else input_list[1]
            # input_memory += 1  # (input_memory + 1) % len(input_list)
        elif instruction == 4:
            out = operands[0]
            return program, i, out
        elif instruction == 5:
            i = (operands[1] - 3) if operands[0] != 0 else i
        elif instruction == 6:
            i = (operands[1] - 3) if operands[0] == 0 else i
        elif instruction == 7:
            program[program[i + 3]] = int(operands[0] < operands[1])
        elif instruction == 8:
            program[program[i + 3]] = int(operands[0] == operands[1])
        i += num_of_operands[instruction] + 1
    return -1, i, out


# in1 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
#        27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
code = in1
settings = list(itertools.permutations([5, 6, 7, 8, 9]))
computers = [code[:], code[:], code[:], code[:], code[:]]
pointers = [0, 0, 0, 0, 0]
best = 0

for s in settings:
    out = 0
    for i, a in enumerate(s):
        print(i, a)
        _, pointers[i], out = run(computers[i], a)
    print(out)
    i = 0
    while True:
        # print(i, out)
        if all([x == -1 for x in computers]):
            break
        while computers[i] == -1:
            print("ok")
            i = (i + 1) % 5
        _, pointers[i], out = run(computers[i], out, pointer=pointers[i])
        i = (i + 1) % 5

    if out > best:
        best = out
    print(best)

print(f"Best: {best}")
# puzzle.answer_a = best
