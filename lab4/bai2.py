#a
a = 2
print("Các số nguyên tố nhỏ hơn 100:")
while a < 100:
    so_nguyen_to = True
    b = 2
    while b <= a // 2:
        if a % b == 0:
            so_nguyen_to = False
            break
        b += 1
    if so_nguyen_to:
        print(a, end=" ")
    a += 1
#b
a = 1
print("\nCác số chính phương nhỏ hơn 100:")
while a < 100:
    b = 1
    so_chinh_phuong = False
    while b * b <= a:
        if b * b == a:
            so_chinh_phuong = True
            break
        b += 1
    if so_chinh_phuong:
        print(a, end=" ")
    a += 1
#c
a, b = 0, 1
print("\nCác số Fibonacci nhỏ hơn 1000:")
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
