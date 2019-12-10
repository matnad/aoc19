lower = 307237
upper = 769058
soln1 = lambda d1, d2: [str(x) for x in range(d1, d2 + 1) if any([str(x)[i] == str(x)[i+1] for i in range(5)]) and not False in ([str(x)[i] <= str(x)[i+1] for i in range(5)])]
print(len(soln1(lower, upper)))