def tong_lap_phuong(n):
    chuoi_so = [int(s) for s in str(n)]
    return sum(so ** 3 for so in chuoi_so)

def in_so_armstrong():
    for num in range(1000):
        if num == tong_lap_phuong(num):
            print(num)

def la_so_armstrong(n):
    return n == tong_lap_phuong(n)

so = 153
print("Tổng các lập phương của các chữ số riêng lẻ của", so, "là:", tong_lap_phuong(so))
print("153 có phải là số Armstrong không?", la_so_armstrong(so))
print("Các số Armstrong từ 0 đến 999:")
in_so_armstrong()