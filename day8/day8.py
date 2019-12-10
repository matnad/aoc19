import numpy as np
from aocd.models import Puzzle
import matplotlib.pyplot as plt
puzzle = Puzzle(year=2019, day=8)
data = puzzle.input_data
W, H = 25, 6
best, ans_a = 1e5, 0
img = np.zeros((H, W), dtype=np.uint8) + 2
for i in range(len(data) // (W * H)):
    layer = list(data[i * W * H: (i + 1) * W * H])
    nplayer = np.array([int(x) for x in layer], dtype=np.uint8).reshape((H, W))
    np.copyto(img, nplayer, where=(img == 2))

    counts = [layer.count(x) for x in '012']
    if counts[0] < best:
        best = counts[0]
        ans_a = counts[1] * counts[2]

print("Part A:", ans_a)
plt.imshow(img, cmap='gray', vmin=0, vmax=2)
plt.show()
