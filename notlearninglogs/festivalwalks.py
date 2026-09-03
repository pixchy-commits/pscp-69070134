""" festival walk """

moves = input().strip()

x = moves.count('E') - moves.count('W')

y = moves.count('N') - moves.count('S')

d = abs(x) + abs(y)

print(f"{x} {y} {d}")
