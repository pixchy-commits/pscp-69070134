"""framer.com"""

lines = [input().rstrip() for _ in range(5)]

max_len = max(len(line) for line in lines)

total_width = max_len + 4

print("*" * total_width)

for line in lines:
    print(f"* {line.ljust(max_len)} *")

print("*" * total_width)
