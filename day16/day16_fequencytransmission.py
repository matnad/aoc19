import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=16)
in1 = puzzle.input_data

print(in1)
# in1 = '80871224585914546619083218645595'
offset = int(''.join(in1[0:7]))
print(offset)

next_signal = in1
siglen = len(in1)
base_pattern = np.array([0, 1, 0, -1])

for phase in range(100):
    signal = np.asarray([int(x) for x in next_signal])
    next_signal = ''
    for r in range(1, siglen + 1):
        pattern = np.repeat(base_pattern, r)
        tilefactor = int(np.ceil((siglen + 1) / len(pattern)))
        pattern = np.tile(pattern, tilefactor)
        mask = np.zeros(len(pattern), dtype=bool)
        mask[1:siglen + 1] = True
        pattern = pattern[mask]
        sigxpat = np.matmul(signal, pattern) * 10000
        next_digit = abs(sigxpat) % 10
        next_signal += str(next_digit)
    # print(next_signal)
# puzzle.answer_a =

ansa = next_signal[0:8]
print(ansa)
puzzle.answer_a = ansa
