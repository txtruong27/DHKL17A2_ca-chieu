n = int(input("Nhập số phần tử của mảng: "))
a = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(num)

print("Các số nguyên tố trong mảng:")
for num in a:
    prime = True
    if num <= 1:
        prime = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

print("Các số hoàn hảo trong mảng:")
for num in a:
    if num <= 1:
        continue
    divisor_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i
    if divisor_sum == num:
        print(num)