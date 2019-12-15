import networkx as nx
from collections import defaultdict
from aocd.models import Puzzle
from day9.day9 import Intcomp

puzzle = Puzzle(year=2019, day=15)
in1 = [int(x) for x in puzzle.input_data.split(',')]

N, S, W, E = range(1, 5)
ERR, OK, GOAL = range(3)
UNKNOWN, WALL, EMPTY, OXYGEN = range(4)
direction_delta = [(x, y) for x, y in zip([0, 0, 0, -1, 1], [0, -1, 1, 0, 0])]
reverse = {d: r for d, r in zip([1, 2, 3, 4], [2, 1, 4, 3])}
grid = defaultdict(int)


def add_dir(point, d):
    """Add a direction delta to a position."""
    return point[0] + direction_delta[d][0], point[1] + direction_delta[d][1]


def show():
    """Draw the grid."""
    xvals, yvals = zip(*[(x, y) for x, y in grid.keys()])
    minx, maxx, miny, maxy = min(xvals), max(xvals), min(yvals), max(yvals)
    for y in range(miny, maxy + 1):
        line = ''
        for x in range(minx, maxx + 1):
            char = grid[x, y]
            if (x, y) == (0, 0):
                line += 'X'
            elif (x, y) == pos:
                line += 'D'
            elif char == UNKNOWN:
                line += ' '
            elif char == EMPTY:
                line += '.'
            elif char == WALL:
                line += '#'
            elif char == OXYGEN:
                line += 'O'
        print(line)
    print('------------------')


pos = (0, 0)
target = (0, 0)
grid[pos] = EMPTY
prog = Intcomp(in1)


def flood_walk(last_dir=0):
    """Recursively explore the grid and update location info."""
    global pos, target
    newpos = [add_dir(pos, d) for d in range(1, 5)]
    explored = [grid[(x, y)] != UNKNOWN for x, y in newpos]
    for d in range(1, 5):
        if not explored[d - 1]:
            prog.run(inp=d, halt_after=1)
            grid[newpos[d - 1]] = prog.out[0] + 1
            if prog.out[0] != ERR:
                if prog.out[0] == GOAL:
                    target = newpos[d - 1]
                pos = add_dir(pos, d)
                flood_walk(d)
    if pos != (0, 0):
        prog.run(inp=reverse[last_dir], halt_after=1)
        pos = add_dir(pos, reverse[last_dir])


flood_walk()
show()
print("Oxygen found at", target)

# Part 1: Contstruct a graph and get the shortest path using dijkstra algorithm
graph = nx.Graph()
for (x, y), v in grid.items():
    if v in [EMPTY, OXYGEN]:
        graph.add_node((x, y))
        nbs = [add_dir((x, y), d) for d in range(1, 5)]
        for nb in nbs:
            if grid[nb] in [EMPTY, OXYGEN]:
                graph.add_edge((x, y), nb)

dijlen = nx.shortest_path_length(graph, source=(0, 0), target=target)
print("Length of shortest path:", dijlen)
# puzzle.answer_a = dijlen


# Part 2: Recursively spread oxygen and track maximum recursion depth which is equal to the time in minutes
def spread(start_pos, time=0, max_time=0):
    """Recursively spread onxygen and keep track of the maximum depth."""
    neighbours = [add_dir(start_pos, d) for d in range(1, 5)]
    for neighbour in neighbours:
        if grid[neighbour] == EMPTY:
            grid[neighbour] = OXYGEN
            max_time = spread(neighbour, time + 1, max_time)
    return max(time, max_time)


total_time = spread(target)
print("Time for oxygen to spread:", total_time)
# puzzle.answer_b = max_time
