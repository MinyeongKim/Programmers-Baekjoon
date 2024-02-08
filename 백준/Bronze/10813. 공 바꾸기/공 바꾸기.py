N, M = map(int,input().split())
#N개의 바구니, M번 교환

basket = [n for n in range(N)]

for m in range(M):
    i, j = map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
    
for x in basket:
    print(f'{x+1}', end=' ') 