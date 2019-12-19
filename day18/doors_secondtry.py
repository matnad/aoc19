from collections import defaultdict, deque
from string import ascii_lowercase, ascii_uppercase
import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=18)
in1 = puzzle.input_data

in1 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

in1 = in1.split('\n')
grid = defaultdict(lambda: '#')
keys = doors = ''
nodepos = {}
start = None

W, H = len(in1[0]), len(in1)
for y in range(H):
    for x in range(W):
        symbol = in1[y][x]
        grid[(x, y)] = symbol
        if symbol in ascii_lowercase:
            keys += symbol
            nodepos[symbol] = (x, y)
        elif symbol in ascii_uppercase:
            doors += symbol
            nodepos[symbol] = (x, y)
        elif symbol == '@':
            start = (x, y)
            nodepos[symbol] = (x, y)

nodes = ['@', *keys, *doors]
node_dist = {node: {} for node in nodes}
to_explore = deque()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for node in nodes:
    visited = defaultdict(bool)
    visited[nodepos[node]] = True
    to_explore.append((nodepos[node], 0))
    while len(to_explore) > 0:
        pos, dist = to_explore.popleft()
        symbol = grid[pos]
        if symbol in nodes and symbol != node:
            node_dist[node][symbol] = dist
        else:
            for i in range(4):
                new_pos = (pos[0] + dx[i], pos[1] + dy[i])
                if grid[new_pos] != '#' and not visited[new_pos]:
                    visited[new_pos] = True
                    to_explore.append((new_pos, dist+1))

print(node_dist)
# print(keypos, doorpos, keys, doors)
#print(grid)
