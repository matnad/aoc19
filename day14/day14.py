from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=14)
in1 = puzzle.input_data.split('\n')

# print(in1)
# in1 = '''10 ORE => 10 A
# 1 ORE => 1 B
# 7 A, 1 B => 1 C
# 7 A, 1 C => 1 D
# 7 A, 1 D => 1 E
# 7 A, 1 E => 1 FUEL'''.split('\n')
# in1 = '''157 ORE => 5 NZVS
# 165 ORE => 6 DCFZ
# 44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
# 12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
# 179 ORE => 7 PSHF
# 177 ORE => 5 HKGWZ
# 7 DCFZ, 7 PSHF => 2 XJWVT
# 165 ORE => 2 GPVTF
# 3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''.split('\n')

rcts = {}
prodq = {}
for line in in1:
    a, b = line.split('=>')
    b = [x.strip() for x in b.split()]
    b = (int(b[0]), b[1])
    a = [a.strip() for a in a.split(',')]
    a = [(int(x[0]), x[1]) for x in [y.split() for y in a]]
    rcts[b[1]] = a
    prodq[b[1]] = b[0]

# print(rcts)
# print(prodq)

ore = 0
store = defaultdict(int)
produced = defaultdict(int)


def prod(ele):
    global ore
    reqs = rcts[ele]
    # print("need", reqs)
    for n, e in reqs:
        if e == 'ORE':
            ore += n
            return
        # print("need", n, e)]
        while store[e] < n:
            prod(e)
            store[e] += prodq[e]
            produced[e] += prodq[e]

        store[e] -= n


capacity = 1000000000000
save = 1e9
use = capacity - save
runs = 5000
for _ in range(runs):
    prod('FUEL')

times = use // ore
remaining = save + use % ore
fuel = runs*times

print(ore, times, remaining, remaining // ore)
print(produced)
print(store)

store = {k: v*times for k, v in store.items()}
print(store)

while remaining > 0:
    ore = 0
    prod('FUEL')
    remaining -= ore
    fuel += 1
    # print(remaining)

print(fuel, remaining)
print(store)

# puzzle.answer_a = ore
puzzle.answer_b = fuel - 1