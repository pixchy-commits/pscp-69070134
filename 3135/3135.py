""" gift thief """

N, K, T = map(int, input().split())

current = 1
count = 1

while True:
    current = (current - 1 + K) % N + 1

    if current == T:
        count += 1
        break

    if current == 1:
        break

    count += 1

print(count)
