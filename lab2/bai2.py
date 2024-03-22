# Nhập số nguyên từ người dùng
so = int(input("Nhập một số nguyên: "))

# Tách chữ số hàng nghìn
tach_ra = (so // 1000) % 10

# Xuất ra chữ số hàng nghìn, nếu không có thì xuất ra 0
if tach_ra != 0:
    print("Chữ số hàng nghìn của số bạn nhập là:", tach_ra)
else:
    print("Số bạn nhập không có chữ số hàng nghìn, nên xuất ra 0.")