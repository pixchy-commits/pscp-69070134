"""
dad
"""
seats = int(input().strip())

while seats > 0:
    line = input().split()
    if not line:
        continue

    age, qty = map(int, line)

    if age < 15:
        print("-1")
    elif qty > seats:
        print("-2")
    else:
        if 15 <= age <= 22:
            price = 120
        elif age >= 60:
            price = 75
        else:
            price = 150

        seats -= qty
        print(f"{price * qty} {seats}")
