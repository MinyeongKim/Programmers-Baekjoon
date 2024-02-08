import sys

while True:
    str = sys.stdin.readline().rstrip('\n')

    if not str: break

    l, u , d, s =  0, 0, 0, 0

    for x in str:
        if x.islower(): l += 1
        elif x.isupper(): u += 1
        elif x.isdigit(): d += 1
        elif x.isspace(): s += 1

    print(l, u, d, s)