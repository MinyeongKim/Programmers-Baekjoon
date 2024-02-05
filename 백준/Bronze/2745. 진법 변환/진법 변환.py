N, B = input().split()
b_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i, x in enumerate(N[::-1]):
    result += (int(B) ** i) * (b_list.index(x))

print(result)