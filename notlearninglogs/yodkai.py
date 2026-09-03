"""yodkai """

N = int(input())

total_sales = 0
max_sales = -1
min_sales = float('inf')

for _ in range(N):
    daily_sales = int(input())

    total_sales += daily_sales

    if daily_sales > max_sales:
        max_sales = daily_sales

    if daily_sales < min_sales:
        min_sales = daily_sales

avg_sales = total_sales / N

print(total_sales)
print(max_sales)
print(min_sales)
print(f"{avg_sales:.1f}")
