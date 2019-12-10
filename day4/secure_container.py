lower = 307237
upper = 769058
ans1, ans2 = [], []

i = lower
while True:
    digits = list(str(i))

    for x in range(5):
        if digits[x] > digits[x + 1]:
            digits[x + 1:6] = digits[x] * (5 - x)
            i = int("".join(digits))
            digits = list(str(i))
            break

    if i > upper:
        break

    counts = list(map(digits.count, digits))
    if 2 in counts:
        ans2.append(i)
    if max(counts) >= 2:
        ans1.append(i)

    i += 1

print(len(ans1), len(ans2))
