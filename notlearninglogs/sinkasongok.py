""" sinka songok """

N = int(input())

total_sum = 0
even_count = 0
odd_count = 0

for _ in range(N):
    stock_value = int(input())

    total_sum += stock_value

    if not stock_value % 2:
        even_count += 1
    else:
        odd_count += 1

print(f"SUM {total_sum}")
print(f"EVEN {even_count}")
print(f"ODD {odd_count}")
