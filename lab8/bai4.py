def sumPdivisors(n):
    tong = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:  
                tong += n // i
    if n == int(n**0.5) * int(n**0.5):
        tong -= int(n**0.5)
    return tong
so = 36
print("Tổng của các ước số chính của", so, "là:", sumPdivisors(so))
