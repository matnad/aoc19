from collections import defaultdict
from aocd.models import Puzzle


class Intcomp():
    def __init__(self, code: list):
        self.code = None
        self.orig_code = None
        self.load(code)
        self.ip = 0
        self.rel_base = 0
        self.num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
        self.out = []

    def load(self, code: list):
        self.orig_code = code
        self.code = defaultdict(int, enumerate(code))

    def set(self, code: list = None, pointer: int = None, base: int = None):
        if code is not None:
            self.load(code)
        self.ip = pointer if pointer is not None else self.ip
        self.rel_base = base if base is not None else self.rel_base

    def reset(self):
        self.set(code=self.orig_code, pointer=0, base=0)
        self.out = []

    def run(self, inp: tuple = None, halt_after=-1):
        self.out = []
        if inp is None:
            inp = (0,)
        inp_i = 0
        while self.code[self.ip] != 99:
            if 0 < halt_after <= len(self.out):
                return self.out
            modes = [int(x) for x in f"{self.code[self.ip]:0>5}"[:3]][::-1]
            instruction = int(f"{self.code[self.ip]:0>5}"[3:])
            operands = [0 for _ in range(self.num_of_operands[instruction])]
            adjust = [0 for _ in range(self.num_of_operands[instruction])]
            for m in range(self.num_of_operands[instruction]):
                if modes[m] == 0:
                    operands[m] = self.code[self.code[self.ip + m + 1]]
                elif modes[m] == 1:
                    operands[m] = self.code[self.ip + m + 1]
                elif modes[m] == 2:
                    adjust[m] = self.rel_base
                    operands[m] = self.code[self.rel_base + self.code[self.ip + m + 1]]

            if instruction == 1:  # ADD
                self.code[adjust[2] + self.code[self.ip + 3]] = operands[0] + operands[1]
            elif instruction == 2:  # MULTIPLY
                self.code[adjust[2] + self.code[self.ip + 3]] = operands[0] * operands[1]
            elif instruction == 3:  # INPUT
                self.code[adjust[0] + self.code[self.ip + 1]] = inp[inp_i]
                inp_i = (inp_i + 1) % len(inp)
            elif instruction == 4:  # OUTPUT
                self.out.append(operands[0])
            elif instruction == 5:  # JUMP IF TRUE
                self.ip = (operands[1] - 3) if operands[0] != 0 else self.ip
            elif instruction == 6:  # JUMP IF FALSE
                self.ip = (operands[1] - 3) if operands[0] == 0 else self.ip
            elif instruction == 7:  # TRUE IS LESS THAN
                self.code[adjust[2] + self.code[self.ip + 3]] = int(operands[0] < operands[1])
            elif instruction == 8:  # TRUE IF EQUAL
                self.code[adjust[2] + self.code[self.ip + 3]] = int(operands[0] == operands[1])
            elif instruction == 9:  # INCREASE RELATIVE BASE
                self.rel_base += operands[0]
            self.ip += self.num_of_operands[instruction] + 1


if __name__ == "__main__":
    puzzle = Puzzle(year=2019, day=9)
    in9 = [int(x) for x in puzzle.input_data.split(',')]

    prog = Intcomp(code=in9)
    prog.run(1)
    print(prog.out, prog.out[-1])
    # puzzle.answer_a = proga.out[-1]

    prog.reset()
    prog.run(2)
    print(prog.out, prog.out[-1])
    # puzzle.answer_b = prog.out[-1]
