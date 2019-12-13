import time
from collections import defaultdict, deque

from aocd.models import Puzzle

from day9.day9 import Intcomp

puzzle = Puzzle(year=2019, day=13)
in1 = [int(x) for x in puzzle.input_data.split(',')]
print(in1)

grid = defaultdict(int)
EMPTY, WALL, BLOCK, PADDLE, BALL = range(5)


def show():
    minx, maxx, miny, maxy = 0, 36, 0, 19
    xv, yv = zip(*grid.keys())
    minx, maxx, miny, maxy = min(xv), max(xv), min(yv), max(yv)
    print(minx, maxx, miny, maxy)
    for y in range(miny, maxy + 1):
        line = ''
        for x in range(minx, maxx + 1):
            char = grid[(x, y)]
            if char == EMPTY:
                line += ' '
            elif char == WALL:
                line += '#'
            elif char == BLOCK:
                line += 'X'
            elif char == PADDLE:
                line += '_'
            elif char == BALL:
                line += 'O'
        print(line)
    print(f"Score: {score}\n")


in1[0] = 2
prog = Intcomp(in1)
i = 0
score = 0
paddle_pos = 0
ball_pos = deque(maxlen=2)
joystick = 0

prog.run(halt_after=3)
while prog.out:
    if i < 740:
        joystick = 0
    x, y, char = prog.out
    if x == -1 and y == 0:
        score = char
    else:
        grid[(x, y)] = char
    i += 1
    if char == BALL:
        ball_pos.append(x)
        if len(ball_pos) == 2 and ball_pos[0] == paddle_pos[0]:
            joystick = ball_pos[1] - ball_pos[0]
        show()
        break
        # time.sleep(0.3)
    elif char == PADDLE:
        paddle_pos = x

    prog.run(inp=joystick, halt_after=3)

show()
blocks = len([1 for x in grid.values() if x == BLOCK])
print(blocks)
# puzzle.answer_a = blocks
# puzzle.answer_b = score