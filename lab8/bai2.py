import math

def hoan_vi(n, r):
    return math.factorial(n) // math.factorial(n - r)

def to_hop(n, r):
    return hoan_vi(n, r) // math.factorial(r)

n = int(input("Nhập giá trị của n: "))
r = int(input("Nhập giá trị của r: "))

print("Số hoán vị của", n, "phần tử lấy", r, "phần tử mỗi lần là:", hoan_vi(n, r))
print("Số tổ hợp của", n, "phần tử lấy", r, "phần tử mỗi lần là:", to_hop(n, r))
