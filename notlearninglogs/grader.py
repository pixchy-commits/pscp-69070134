""" grade checker """

N = int(input())

total_score = 0
is_all_passed = True

for _ in range(N):
    score = int(input())
    total_score += score

    if score < 50:
        is_all_passed = False

average = total_score / N

print(f"{average:.1f}")

if is_all_passed and average >= 60.0:
    print("PASS")
else:
    print("FAIL")
