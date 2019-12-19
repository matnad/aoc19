from collections import defaultdict

from aocd.models import Puzzle

from day9.day9 import Intcomp

puzzle = Puzzle(year=2019, day=19)
in1 = [int(x) for x in puzzle.input_data.split(',')]
calls = 0


def check(point):
    prog.reset()
    prog.run(inp=point)
    return prog.out[0] if prog.out else None


prog = Intcomp(in1)
x = box = 100
for y in range(box, 99999):
    while check((x, y)) == 0: x += 1
    if check((x+box-1, y-box+1)) == 1: break

print(f"Closest point to fit santa's ship {(x, y-99)}: {x * 10000 + y-99}")
# puzzle.answer_b = ansb

# def show():
#     global ansa
#     last_row = 0
#     for y in range(dim):
#         line_nr = ' ' * (3 - len(str(y))) + str(y)
#         last_row = ' ' * (3 - len(str(last_row))) + str(last_row)
#         line = f'{line_nr} {last_row}'
#         first = True
#         last_row = 0
#         for x in range(dim):
#             if grid[(x, y)] == 1:
#                 line += '#'
#                 last_row = x if first else last_row
#                 first = False
#                 ansa += 1
#             else:
#                 line += '.'
#         print(line)


# ansa = 0
# show()
# print(ansa)
# puzzle.answer_a = ansa
