chuoi = input("Nhập chuỗi: ")
a = 0
b = 0
c = 0
d = 0

for char in chuoi:
    if char.islower():
        a += 1
    elif char.isupper():
        b += 1
    elif char.isdigit():
        c += 1
    else:
        d += 1

print("Số lượng chữ thường:", a)
print("Số lượng chữ hoa:", b)
print("Số lượng chữ số:", c)
print("Số lượng ký tự đặc biệt:",d)
