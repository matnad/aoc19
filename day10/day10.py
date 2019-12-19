from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=10)
in10 = puzzle.input_data.split('\n')

# in10 = '''#.#...#.#.
# .###....#.
# .#....#...
# ##.#.#.#.#
# ....#.#.#.
# .##..###.#
# ..#...##..
# ..##....##
# ......#...
# .####.###.'''.split('\n')

in10 = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''.split('\n')

print(in10)

allblocks = 0
A = defaultdict(bool)
for y, line in enumerate(in10):
    for x, char in enumerate(line):
        A[(x, y)] = char == '#'
        if char == '#':
            allblocks += 1
W = x+1
H = y+1
print(A)
print(allblocks, x, y)


def project(a, b, d):
    if a[0] == b[0]:
        if a[1] > b[1]:
            d = -d
        mod = -1 if d > 0 else 1
        return b[0], b[1] + d + mod
    elif a[1] == b[1]:
        if a[0] > b[0]:
            d = -d
        mod = -1 if d > 0 else 1
        return b[0] + d + mod, b[1]
    else:
        return a[0] + d * (b[0] - a[0]), a[1] + d * (b[1] - a[1])


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
            if c[0] >= W or c[0] < 0 or c[1] >= H or c[1] < 0:
                break
            if A[c]:
                blocked[c] = True
                # print(a,b,dist,c)
            dist += 1

    # print("blocked",len(blocked),blocked)
    # if a == (1,2):
    #    print(blocked)
    #    print(len(blocked), total - 1 - len(blocked))

    detected[a] = allblocks - 1 - len(blocked)
    if a == (11,13):
        print(W,H,A)
        print(detected[a], blocked)
        for j in range(H):
            line = ''
            for k in range(W):
                if A[(k, j)]:
                    if a == (k, j):
                        line += 'A'
                    elif blocked[(k, j)]:
                        line += 'X'
                    else:
                        line += '#' #str(k)
                else:
                    line += '.'
            print(line)
        break

srt = sorted(detected, key=detected.get, reverse=True)
# print(detected)
best = srt[0]
print("total", allblocks)
print(best, detected[best])
# print(project((0, 0), (3, 1), -2))
# puzzle.answer_a = detected[best]
