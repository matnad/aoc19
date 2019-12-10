import numpy as np


def build_paths(paths):
    boxinfo = get_box(paths)
    b = np.zeros((boxinfo['height'], boxinfo['width']))
    print(boxinfo)
    numbered_path1 = count_box(boxinfo, paths[0])
    numbered_path2 = count_box(boxinfo, paths[1])


    i = 0
    for path in paths:
        i += 1
        y = boxinfo['height'] - 1 - boxinfo['yshift']
        x = boxinfo['xshift']
        origin = (y, x)
        b[y, x] = -1
        for instruction in path:
            direction = instruction[0]
            dist = int(instruction[1:])
            if direction == 'R':
                b[y, x + 1:x + dist + 1] += i
                x += dist
            elif direction == 'L':
                b[y, x - dist:x] += i
                x -= dist
            elif direction == 'U':
                b[y - dist:y, x] += i
                y -= dist
            elif direction == 'D':
                b[y + 1:y + dist + 1, x] += i
                y += dist
        if i == 1:
            b[b > 1] = 1
    x, y = np.where((b >= 3) & (b % 2 == 1))
    cross = []
    for i, v in enumerate(x):
        cross.append((v, y[i]))

    print(len(cross))

    best_point = 0
    best_dist = np.inf
    for i, p in enumerate(cross):
        # dist = man_dist(origin, p)
        dist = circuit_dist(p, numbered_path1, numbered_path2)
        if dist < best_dist:
            best_dist = dist
            best_point = i

    return cross[best_point], best_dist


def count_box(boxinfo, path):
    b = np.zeros((boxinfo['height'], boxinfo['width']))
    y = boxinfo['height'] - 1 - boxinfo['yshift']
    x = boxinfo['xshift']
    i = 1
    b[y,x] = -1
    for instruction in path:
        direction = instruction[0]
        dist = int(instruction[1:])
        if direction == 'R':
            for s in range(dist):
                b[y, x + s + 1] = i
                i += 1
            x += dist
        elif direction == 'L':
            for s in range(dist):
                b[y, x - s - 1] = i
                i += 1
            x -= dist
        elif direction == 'U':
            for s in range(dist):
                b[y - s - 1, x] = i
                i += 1
            y -= dist
        elif direction == 'D':
            for s in range(dist):
                b[y + s + 1, x] = i
                i += 1
            y += dist
    return b


def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def circuit_dist(a, box1, box2):
    return box1[a] + box2[a]


def get_box(paths):
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for path in paths:
        x_pos = 0
        y_pos = 0
        for instruction in path:
            direction = instruction[0]
            distance = int(instruction[1:])
            if direction == 'R':
                x_pos += distance
            elif direction == 'L':
                x_pos -= distance
            elif direction == 'U':
                y_pos += distance
            elif direction == 'D':
                y_pos -= distance

            if x_pos < min_x:
                min_x = x_pos
            elif x_pos > max_x:
                max_x = x_pos
            elif y_pos < min_y:
                min_y = y_pos
            elif y_pos > max_y:
                max_y = y_pos

    return {
        'width': abs(min_x) + abs(max_x) + 1,
        'height': abs(min_y) + abs(max_y) + 1,
        'xshift': abs(min_x),
        'yshift': abs(min_y)
    }


with open("input3.txt") as file:
    in_paths = [line.strip().split(",") for line in file]

print(build_paths(in_paths))
