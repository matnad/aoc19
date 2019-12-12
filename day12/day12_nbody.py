import re
from math import gcd
from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=12)
in1 = puzzle.input_data.split('\n')

# in1 = '''<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>'''.split('\n')
# in1 = '''<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>'''.split('\n')


class Moon:
    def __init__(self, pos, velo=None, name=None):
        if velo is None:
            velo = [0] * len(pos)
        self.position = pos
        self.velocity = velo
        self.name = name

    def apply_gravity(self, other):
        for axis in range(len(self.position)):
            if self.position[axis] < other.position[axis]:
                self.velocity[axis] += 1
            elif self.position[axis] > other.position[axis]:
                self.velocity[axis] -= 1

    def apply_velocity(self):
        for axis in range(len(self.velocity)):
            self.position[axis] += self.velocity[axis]

    def get_energy(self):
        return sum([abs(x) for x in self.position]) * sum([abs(x) for x in self.velocity])

    def get_state(self, axis):
        return self.position[axis], self.velocity[axis]

    def __repr__(self):
        return f"{self.name} p{self.position} v{self.velocity}"


def lcm(x, y):
    return x * y // gcd(x, y)


# create moons
moons = []
names = ["Io", "Europa", "Ganymede", "Callisto"]
for i, line in enumerate(in1):
    coords = [int(x) for x in re.findall(r'-?\d+', line)]
    moons.append(Moon(coords, name=names[i]))


# run simulation and store states
prev_states = [defaultdict(bool) for _ in range(3)]
iterations_per_axis = [0, 0, 0]
it = 0
while True:
    for moon1 in moons:
        for moon2 in moons:
            if moon1.name != moon2.name:
                moon1.apply_gravity(moon2)
    for moon in moons:
        moon.apply_velocity()

    states = [tuple([m.get_state(ax) for m in moons]) for ax in range(3)]
    for ax in range(3):
        if iterations_per_axis[ax] == 0:
            if prev_states[ax][states[ax]]:
                iterations_per_axis[ax] = it
            prev_states[ax][states[ax]] = True
    if all([x > 0 for x in iterations_per_axis]):
        break
    it += 1

energy = [m.get_energy() for m in moons]
print("total energy:", sum(energy))
lcm_of_axes = lcm(iterations_per_axis[0], lcm(iterations_per_axis[1], iterations_per_axis[2]))
print(lcm_of_axes)
# puzzle.answer_a = sum(energy)
puzzle.answer_b = lcm_of_axes
