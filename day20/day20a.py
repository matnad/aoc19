from collections import defaultdict
from string import ascii_uppercase

import networkx as nx
from aocd.models import Puzzle


def get_nbs(point):
    """Get all four neighbouring points."""
    return [(point[0] + dx, point[1] + dy) for dx, dy in zip([0, 1, 0, -1], [-1, 0, 1, 0])]


puzzle = Puzzle(year=2019, day=20)
in1 = puzzle.input_data.split('\n')

grid = defaultdict(lambda: '#')
W, H = len(in1[0]), len(in1)

for y in range(H):
    for x in range(W):
        grid[(x, y)] = in1[y][x] if in1[y][x] != ' ' else '#'

portals = defaultdict(list)  # matches the portal names to their coordinates like portals['XY'] = [(x1,y1), (x2, y2)]
G = nx.Graph()
start = end = None
for y in range(1, H - 1):
    for x in range(1, W - 1):
        symbol = grid[(x, y)]
        if symbol in ascii_uppercase:
            nbs = [(a, b) for a, b in get_nbs((x, y)) if grid[(a, b)] != '#']
            if len(nbs) == 2:
                # letter and pathway found
                if grid[nbs[0]] in ascii_uppercase:
                    letter, pad = nbs
                else:
                    pad, letter = nbs
                key = ''.join(sorted(symbol + grid[letter]))  # sort portal name
                portals[key].append(pad)
                if key == 'AA':
                    start = pad
                elif key == 'ZZ':
                    end = pad
        elif symbol == '.':
            G.add_node((x, y))
            nbs = [(a, b) for a, b in get_nbs((x, y)) if grid[(a, b)] == '.']
            for nb in nbs:
                G.add_edge((x, y), nb)  # connect pathways

for pads in portals.values():
    if len(pads) == 2:
        G.add_edge(pads[0], pads[1])  # connect portals

ansa = len(nx.shortest_path(G, start, end)) - 1
print("Number of steps to get from AA to ZZ:", ansa)
# puzzle.answer_a = ansa
