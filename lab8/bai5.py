def sum_divisors(n):
    tong = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    if n == int(n**0.5) * int(n**0.5):
        tong -= int(n**0.5)
    return tong
def la_so_amicable(a, b):
    return sum_divisors(a) == b and sum_divisors(b) == a and a != b
so1 = 220
so2 = 284
if la_so_amicable(so1, so2):
    print(so1, "và", so2, "là một cặp số amicable.")
else:
    print(so1, "và", so2, "không phải là một cặp số amicable.")
