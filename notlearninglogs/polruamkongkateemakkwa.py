""" pol ruam kongka teemakkwa """

n = int(input())

max_values = []

for _ in range(n):
    a = int(input())
    b = int(input())

    max_values.append(max(a, b))

if n == 1:
    print(max_values[0])
else:
    str_max_vals = [str(val) for val in max_values]
    equation_left = " + ".join(str_max_vals)
    total_sum = sum(max_values)

    print(f"{equation_left} = {total_sum}")
