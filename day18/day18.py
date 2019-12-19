from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=18)
in1 = puzzle.input_data
# in1 = '''########################
# #f.D.E.e.C.b.A.@.a.B.c.#
# ######################.#
# #d.....................#
# ########################'''
# in1 = '''########################
# #...............b.C.D.f#
# #.######################
# #.....@.a.B.c.d.A.e.F.g#
# ########################'''
# in1 = '''#################
# #i.G..c...e..H.p#
# ########.########
# #j.A..b...f..D.o#
# ########@########
# #k.E..a...g..B.n#
# ########.########
# #l.F..d...h..C.m#
# #################'''
# in1 = '''########################
# #@..............ac.GI.b#
# ###d#e#f################
# ###A#B#C################
# ###g#h#i################
# ########################'''
in1 = in1.split('\n')

grid = defaultdict(lambda: '.')
keys = ''
doors = ''
keyc = {}
doorc = {}
start = None
collected = []

W, H = len(in1[0]), len(in1)
for y in range(H):
    for x in range(W):
        v = in1[y][x]
        grid[(x, y)] = v
        if v in ascii_lowercase:
            keys += v
            keyc[v] = (x, y)
        elif v in ascii_uppercase:
            doors += v
            doorc[v] = (x, y)
        elif v == '@':
            start = (x, y)


def show():
    for y in range(H):
        line = ''
        for x in range(W):
            line += grid[(x, y)]
        print(line)


def get_nbs(point, mode='cross'):
    x, y = point
    if mode == 'cross':
        return [(x + a, y + b) for a, b in [(0, -1), (1, 0), (0, 1), (-1, 0)]]  # URDL


G1 = nx.Graph()
for y in range(H):
    for x in range(W):
        v = grid[(x, y)]
        if v != '#':
            G1.add_node((x, y))
            for nb in [(x, y) for x, y in get_nbs((x, y)) if grid[(x, y)] != '#']:
                G1.add_edge((x, y), nb)

# print(nx.shortest_path_length(G1, keyc['a'], doorc['A']))

# G2 = nx.DiGraph()
# for y in range(H):
#     for x in range(W):
#         v = grid[(x, y)]
#         if v in '#.':
#             continue
#         level = 0
#         if v in keys:
#             nx.shortest_path_length(G1, start, (x,y))
#             G1.add_node((x, y, level))
#
#         elif v in doors:
#             level = doors.find(v) + 1
#             G1.add_node((x, y, level))

key_blocked_by = {}
distances = {}
for key in keys:
    path = list(nx.shortest_path(G1, start, keyc[key]))
    blocked_by = set(doors)
    for door in doors:
        if doorc[door] not in path:
            blocked_by.remove(door)
    key_blocked_by[key] = [x.lower() for x in blocked_by]
    distances[('start', key)] = len(path) - 1


# print(distances)


def get_blocked_by(key):
    global allblocks
    bb = key_blocked_by[key]
    if not bb:
        return
    for k in bb:
        allblocks.add(k)
        get_blocked_by(k)


full_blocks = {}
for key in keys:
    allblocks = set()
    get_blocked_by(key)
    full_blocks[key] = allblocks


def get_distance(a, b):
    """Caching distances."""
    dist = distances.get((a, b), None)
    if not dist:
        dist = nx.shortest_path_length(G1, keyc[a], keyc[b])
        distances[(a, b)] = dist
    # print("distance", a , b, dist)
    return dist


def crawl(last_node, collected, distance):
    global solutions
    if len(collected) == len(keys):
        solutions.append(distance)
        # print(path, distance)
        return
    reachable = [k for k in keys if full_blocks[k].issubset(collected) and k not in collected]

    for r in reachable:
        new_collected = collected.copy()
        new_collected.add(r)
        # path.append((r, get_distance(last_node, r)))
        # print(last_node, reachable, r, new_collected, get_distance(last_node, r), distance, path)
        crawl(r, new_collected, distance + get_distance(last_node, r))


print(full_blocks)
collected = set()
solutions = []
crawl('start', collected, 0)
print(solutions)
print("best route", min(solutions))
show()
# for key, bb in sorted(full_blocks, key=len(full_blocks.get) :
# print(sorted(full_blocks, key=lambda x: len(full_blocks.get(x))))
# last_key = 'start'
# last_value = 0
# for i in range(len(keys)):
#     keys_in_stage = {k: v for k, v in full_blocks.items() if len(v) == i}
#     for k, v in keys_in_stage.items():
#         v = tuple(v)
#         # G2.add_node((k, v))
#         G2.add_edge((last_key, last_value), (last_key, v))
#         last_key = k
#         last_value = v
#
# print(G2.edges)
# # G2.add_node(('start', set()))
# for key in keys:
#     G2.add_node((key, ))

#
# for key in keys:
#     for other in keys:
#         if key == other:
#             continue
#         distance = nx.shortest_path_length(G1, keyc[key], keyc[other])
#         resolved_blocks = full_blocks[key].copy()
#         G2.add_node((key, tuple(resolved_blocks.copy())))
#         resolved_blocks.add(key)
#         fullblocks = full_blocks[other]
#         remaining = list(set(fullblocks) - set(resolved_blocks))
#         if key == 'c':
#             print(other, fullblocks, resolved_blocks, remaining, len(remaining))
# if len(remaining) == 0:
#     G2.add_edge(key, other, weight=distance)
# else:
#     G2.add_edge(other, key, weight=distance)

# G2.add_edge(key, 'start', weight=nx.shortest_path_length(G1, start, keyc[key]))
# if len(full_blocks[key]) == 0:
#     G2.add_edge('start', key, weight=nx.shortest_path_length(G1, start, keyc[key]))

# print(full_blocks)
# print(G2.nodes)
# print(nx.shortest_path(G2, 'start', 'f'))

# print(key_blocked_by)
# show()
# puzzle.answer_a =
# {'f': {'E', 'C', 'D', 'A'}, 'e': {'C', 'A'}, 'b': {'A'}, 'a': set(), 'c': {'B'}, 'd': {'B'}}
