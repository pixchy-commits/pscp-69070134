"""  สูตรนี้ มีพระเจ้ามามอบให้ผมครับผมฝันเมื่อคืนว่าพระเจ้ามาให้สูตรนี้ผมเลยเอามาเขียนเป็นโค้ดครับ
    สูตรนี้เป็นสูตรที่ใช้ในการหาจำนวนครั้งที่ต้องทำการกระโดด """

import math

X, Y = map(int, input().split())

n_max = (X + 1) // 2
max_dist = n_max * X - n_max * (n_max - 1)

if max_dist < Y:
    print(-1)
else:
    discriminant = (X + 1) ** 2 - 4 * Y
    root = math.isqrt(discriminant)

    if root * root == discriminant:
        n = ((X + 1) - root + 1) // 2
    else:

        n = ((X + 1) - root) // 2

    print(n)
