from functools import reduce
from operator import mul
from steves_utilities.profiler import profile

def check_high(these, high):
    if not these:
        return high
    prod = reduce(mul, these, 1)
    return prod if prod > high else high

@profile
def project_euler_11(x, y):
    grid = [[int(z) for z in y.strip().split()] for y in open(x).readlines()]
    high, rows, cols = 0, len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if c < cols - y + 1:
                high, ua, da = check_high(grid[r][c:c + y], high), [], []
                for i in range(y):
                    if r > 3:
                        ua.append(grid[r - i][c + i])
                    if r < rows - y + 1:
                        da.append(grid[r + i][c + i])
                high = check_high(ua, high)
                high = check_high(da, high)
            if r < rows - y + 1:
                d = []
                for i in range(y):
                    d.append(grid[r + i][c])
                high = check_high(d, high)
    return high
print('answer for problem 11: %d' % project_euler_11('./can/project_euler_11.txt', 4))