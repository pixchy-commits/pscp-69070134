"""13 chun program."""


def main():
    """Decode room number based on secret 5-digit number."""
    s = input().strip().zfill(5)
    d = [int(c) for c in s]

    # หลักแรก
    if d[0] > 5:
        p1 = "9"
    elif d[1] > 5:
        p1 = "10"
    elif d[2] > 5:
        p1 = "11"
    elif d[3] > 5:
        p1 = "12"
    elif d[4] > 5:
        p1 = "14"
    else:
        p1 = "13"

    # หลักที่สอง
    is_palin = s == s[::-1]

    if is_palin:
        if d[0] + d[4] > 5:
            p2 = "1"
        elif d[1] * d[3] > 5:
            p2 = "2"
        else:
            p2 = "0"
    else:
        div_res = (d[0] // d[4]) if d[4] else 0
        if div_res > 5:
            p2 = "1"
        elif d[1] - d[4] > 5:
            p2 = "2"
        else:
            p2 = "0"

    # หลักที่สาม
    sum_all = sum(d)
    prod_all = 1
    for x in d:
        prod_all *= x

    if sum_all > 25:
        p3 = "1"
    elif prod_all > 55:
        p3 = "2"
    else:
        p3 = "0"

    print(f"{p1}{p2}{p3}")


if __name__ == "__main__":
    main()