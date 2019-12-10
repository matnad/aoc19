from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=10)
in10 = puzzle.input_data.split('\n')

in10 = '''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.'''.split('\n')
print(in10)

total = 0
A = defaultdict(bool)
for y, line in enumerate(in10):
    for x, char in enumerate(line):
        A[(x, y)] = char == '#'
        if char == '#':
            total += 1
W = x
H = y
print(A)
print(total, x, y)


def project(a, b, d):
    return a[0] + d * (b[0] - a[0]), a[0] + d * (b[1] - a[1])


detected = defaultdict(int)
for a, isA in A.items():
    # print(a, isA)
    blocked = defaultdict(bool)
    if not isA:
        continue

    for b, isB in A.items():
        if not isB or a == b:
            continue
        c = b
        dist = 2
        while True:
            c = project(a, b, dist)
            if c[0] > W or c[0] < 0 or c[1] > H or c[1] < 0:
                break
            if A[c]:
                blocked[c] = True
            dist += 1
        dist = -2
        while True:
            c = project(a, b, dist)
            if c[0] > W or c[0] < 0 or c[1] > H or c[1] < 0:
                break
            if A[c]:
                blocked[c] = True
            dist -= 1

    # print("blocked",len(blocked),blocked)
    if a == (2,9):
        print(blocked)
    detected[a] = total - 1 - len(blocked)


srt = sorted(detected, key=detected.get, reverse=True)
best = srt[0]
print(best, detected[best])
# print(project((0, 0), (3, 1), -2))
# puzzle.answer_a =
