import math
# Nhập đường thẳng
print("Nhập thôngsố của đường thẳng:")
a = float(input("Nhập hệ số góc (a): "))
b = float(input("Nhập hệ số tự do (b): "))
# Nhập số của đường tròn
print("Nhập số của đường tròn:")
x_tam = float(input("Nhập tọa độ x của tâm đường tròn: "))
y_tam = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))
# Tính khoảng cách từ tâm của đường tròn đến đường thẳng
khoang_cach = abs(b - y_tam) / math.sqrt(a ** 2 + 1)
# Kiểm tra 
if khoang_cach < ban_kinh:
    print("\nĐường thẳng cắt đường tròn.")
elif khoang_cach == ban_kinh:
    print("\nĐường thẳng tiếp xúc đường tròn.")
else:
    print("\nĐường thẳng nằm ngoài đường tròn.")