#a
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
fibonacci = [0, 1] if n >= 2 else [0] if n == 1 else []

[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(n - 2)]

print("Dãy Fibonacci:", fibonacci)

#b
so_nguyen_to = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

print("Danh sách số nguyên tố nhỏ hơn 100:",  so_nguyen_to)
