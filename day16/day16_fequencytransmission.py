import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=16)
in1 = puzzle.input_data

print(in1)
# in1 = '80871224585914546619083218645595'
in1 = '1234567890123'
# offset = int(''.join(in1[0:7]))
# print(offset)

next_signal = in1
siglen = len(in1)
base_pattern = np.array([0, 1, 0, -1])

for phase in range(1):
    signal = np.asarray([int(x) for x in next_signal])
    next_signal = ''
    for r in range(1, siglen*1000 + 1):
        pattern = np.repeat(base_pattern, r)
        tilefactor = int(np.ceil((siglen*1000 + 1) / len(pattern)))
        # print(tilefactor)
        pattern = np.tile(pattern, tilefactor)
        pattern = pattern[1:siglen*1000+1]
        # print("len pat", len(pattern))
        patterns = np.split(pattern, 1000)
        patsum = sum(patterns)
        # print(patterns)
        # print(patsum)
        # print(pattern_offset, signal, pattern[0:siglen], pattern[siglen:2*siglen], pattern[2*siglen:3*siglen])
        # mask = np.zeros(len(pattern), dtype=bool)
        # mask[1:siglen + 1] = True
        # pattern = pattern[mask]
        # print(signal, pattern)
        sigxpat = np.matmul(signal, patsum)
        next_digit = abs(sigxpat) % 10
        next_signal += str(next_digit)
        # print(next_signal)
    print(next_signal)
# puzzle.answer_a =

# ansa = next_signal[0:8]
# print(ansa)
# puzzle.answer_a = ansa
