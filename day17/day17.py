from collections import defaultdict

from aocd.models import Puzzle

from day9.day9 import Intcomp

puzzle = Puzzle(year=2019, day=17)
in1 = [int(x) for x in puzzle.input_data.split(',')]

SCAFFOLD = 35
directions = {d: p for d, p in (zip(range(4), [(0, -1), (1, 0), (0, 1), (-1, 0)]))}
U, R, D, L = range(4)

prog = Intcomp(in1)
prog.run()
print(prog.out)

W, H = 49, 42

grid = defaultdict(lambda: 46)
y, x = 0, 0
for ordv in prog.out:
    if ordv == 10:
        y += 1
        x = 0
    else:
        grid[(x, y)] = ordv
        x += 1


def show():
    for y in range(H):
        line = ''
        for x in range(W):
            if (x, y) in corners:
                line += 'C'
            elif (x, y) == goal:
                line += 'G'
            elif (x, y) in intersections:
                line += 'O'
            else:
                line += chr(grid[(x, y)])
        print(line)


def get_nbs(point, mode='cross'):
    x, y = point
    if mode == 'cross':
        return [(x + a, y + b) for a, b in [(0, -1), (1, 0), (0, 1), (-1, 0)]]  # URDL


def dir_turn(dir, turn):
    mod = 1 if turn == 'R' else -1
    return (dir + mod) % 4


intersections = []
corners = []
ansa = 0
for y in range(H):
    for x in range(W):
        neighbouring_scaffolds = grid[(x, y)] == SCAFFOLD and sum([grid[c] == SCAFFOLD for c in get_nbs((x, y))])
        if neighbouring_scaffolds >= 4:
            intersections.append((x, y))
            ansa += x * y
        elif neighbouring_scaffolds == 2 and grid[(x - 1, y)] != grid[(x + 1, y)]:
            corners.append((x, y))


def to_next_inter(pos, cmds: list, blocked: defaultdict, turn, dir):
    blocked = blocked.copy()
    cmds = cmds.copy()
    # print(pos, cmds, turn, dir)
    if turn:
        dir = dir_turn(dir, turn)

    move_dir = directions[dir]
    pathlen = 0
    done = False
    # print(new_dir, move_dir)
    if len(cmds) >= 18:
        pathlist.append(cmds)
        return
    if pos == goal:
        pathlist.append(cmds)
        return
    while not done:
        nb = pos[0] + move_dir[0], pos[1] + move_dir[1]
        pathlen += 1
        blocked[pos] = True
        if nb in corners or nb in intersections:
            done = True
            cmds.extend([turn, pathlen])
            new_pos = [(a, b) for a, b in get_nbs(nb) if
                       (a, b) != pos and grid[(a, b)] == SCAFFOLD and not blocked[(a, b)]]
            if len(new_pos) == 0:
                return
            for new in new_pos:
                if dir == U:
                    turn = 'R' if nb[0] < new[0] else 'L'
                    turn = None if nb[1] > new[1] else turn
                elif dir == R:
                    turn = 'R' if nb[1] < new[1] else 'L'
                    # turn = None if nb[1] > new[1] else turn
                elif dir == D:
                    turn = 'R' if nb[0] > new[0] else 'L'
                elif dir == L:
                    turn = 'R' if nb[1] > new[1] else 'L'
                # print("TURN", turn, pos, new)
                print(pos, cmds)
                to_next_inter(nb, cmds, blocked, turn, dir)
        pos = nb
    # return path


start = (12, 20)
goal = (40, 41)
show()
pathlist = []
to_next_inter(start, [], defaultdict(bool), 'L', U)
for path in pathlist:
    print(path)
# print(len(intersections), intersections)
# print(ansa)
# puzzle.answer_a = ansa
