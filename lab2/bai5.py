# Giá vé 1 người
gia_ve = 120000

# Nhập số lượng người 
so_luong_nguoi = int(input("Nhập số lượng người: "))

# Tính tổng số tiền trước khi giảm giá
tong_tien = so_luong_nguoi * gia_ve

# Áp dụng giảm giá dựa trên số người
if so_luong_nguoi >= 2 and so_luong_nguoi < 4:
    tong_tien *= 0.95  
elif so_luong_nguoi >= 4 and so_luong_nguoi < 10:
    tong_tien *= 0.9  
elif so_luong_nguoi >= 10:
    tong_tien *= 0.8  

# In ra 
print("Tổng số tiền phải trả là:", tong_tien, "đồng.")