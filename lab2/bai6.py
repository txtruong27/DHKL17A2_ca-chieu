# Nhập số
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
# Tìm số lớn thứ hai
so_lon_thu_2 = None
if a >= b and a >= c:
    if b >= c:
        so_lon_thu_2 = b
    else:
        so_lon_thu_2 = c
elif b >= a and b >= c:
    if a >= c:
         so_lon_thu_2= a
    else:
        so_lon_thu_2 = c
else:
    if a >= b:
        so_lon_thu_2 = a
    else:
        so_lon_thu_2 = b
# In ra
print("Số lớn thứ hai là:", so_lon_thu_2)
