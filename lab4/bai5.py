import math
while True:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b
    luy_thua = a ** b
    can_bac_hai_so_nhat = math.sqrt(a)
    can_bac_hai_so_hai = math.sqrt(b)
    print("Kết quả các phép tính:")
    print("Tổng:", tong)
    print("Hiệu:", hieu)
    print("Tích:", tich)
    print("Thương:", thuong)
    print("Lũy thừa:", luy_thua)
    print("Căn bậc hai của số thứ nhất:", can_bac_hai_so_nhat)
    print("Căn bậc hai của số thứ hai:", can_bac_hai_so_hai)
    choice = input("Bạn có muốn tiếp tục không? (yes/no): ")
    if choice.lower() != 'yes':
        break
