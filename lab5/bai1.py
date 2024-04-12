a = int(input("Nhập số nguyên dương (thập phân): "))
while a <= 0:
    print("Vui lòng nhập một số nguyên dương.")
    a = int(input("Nhập số nguyên dương (thập phân): "))
b = bin(a).replace("0b", "")
print("Số nhị phân tương ứng là:", b)
