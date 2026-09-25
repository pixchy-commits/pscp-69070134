"""
ผลรวมอนุกรม n(n+1)/2 
"""
L, N = map(int, input().split())
k = 1
while (k * L) * (k * L + 1) // 2 < N:
    k += 1
print(k)
