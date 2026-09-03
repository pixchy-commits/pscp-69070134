""" prime number finder """

def is_prime(n):
    """ check if n is prime """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

init, end = map(int, input().split())
primes = []

start_num = min(init, end)
end_num = max(init, end)

for x in range(start_num, end_num + 1):
    if is_prime(x):
        primes.append(str(x))

if primes:
    print(" ".join(primes))

print("Total primes:", len(primes))
