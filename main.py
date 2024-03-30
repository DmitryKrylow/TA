m,d = map(int, input().split())

def fast_pow(x, y):
    s, v, c = 1, y, x
    while (v > 0):
        if (v % 2 == 1):
            s = s * c
        v = v >> 1
        c = c * c
    return s

ranges = 1000000001
while True:
    if (fast_pow())