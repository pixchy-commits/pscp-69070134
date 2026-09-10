"""gambling"""

win_letter, win_num = input().split()
my_letter, my_num = input().split()

is_letter_match = win_letter == my_letter

if win_num == my_num:
    if is_letter_match:
        print(1000000)
    else:
        print(100000)
elif win_num[-3:] == my_num[-3:]:
    if is_letter_match:
        print(2000)
    else:
        print(200)
elif win_num[-2:] == my_num[-2:]:
    if is_letter_match:
        print(1000)
    else:
        print(100)
elif is_letter_match:
    print(20)
else:
    print(0)
