import heapq
from collections import defaultdict, deque
from string import ascii_lowercase, ascii_uppercase
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=18)
in1 = puzzle.input_data

# in1 = '''#################
# #i.G..c...e..H.p#
# ########.########
# #j.A..b...f..D.o#
# ########@########
# #k.E..a...g..B.n#
# ########.########
# #l.F..d...h..C.m#
# #################'''

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
                    to_explore.append((new_pos, dist + 1))

# print(node_dist)
bf_dist = {node: {} for node in nodes}
bf_dist['@'][0] = 0

pq = [(0, 0, '@')]
heapq.heapify(pq)

key_int_dict = {key: 1 << i for i, key in enumerate(keys)}
full_keys = (1 << len(keys)) - 1

while len(pq) != 0:
    dist, key_map, node = heapq.heappop(pq)
    if key_map == full_keys:
        print(dist)
        break
    # print(node_dist[node])
    for next_node in node_dist[node]:
        new_dist = dist + node_dist[node][next_node]
        next_key_map = key_map
        if next_node.isupper() and key_int_dict[next_node.lower()] & next_key_map == 0:
            # key not yet obtained
            continue
        elif next_node.islower():
            # add key
            next_key_map |= key_int_dict[next_node]
        if next_key_map not in bf_dist[next_node] or new_dist < bf_dist[next_node][next_key_map]:
            bf_dist[next_node][next_key_map] = new_dist
            heapq.heappush(pq, (new_dist, next_key_map, next_node))

# puzzle.answer_a = dist
