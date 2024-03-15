import math

def tinh_dien_tich_xung_quanh(a, h):
    l = math.sqrt(a**2 + h**2)  # tính độ dài cạnh nghiêng
    S = 0.5 * a * l             # diện tích một mặt tam giác
    return 4 * S                 # diện tích xung quanh là 4 lần diện tích một mặt tam giác

def tinh_dien_tich_toan_phan(a, h):
    l = math.sqrt(a**2 + h**2)  # tính độ dài cạnh nghiêng
    S = 0.5 * a * l             # diện tích một mặt tam giác
    return S * 4 + a**2 * math.sqrt(3)  # diện tích toàn phần bao gồm diện tích xung quanh và diện tích đáy

def tinh_the_tich(a, h):
    return (a**2 * h * math.sqrt(3)) / 4  # công thức tính thể tích của hình chóp tứ giác đều

def main():
    try:
        a = float(input("Nhập độ dài cạnh đáy của hình chóp tứ giác đều: "))
        h = float(input("Nhập chiều cao của hình chóp tứ giác đều: "))

        dien_tich_xung_quanh = tinh_dien_tich_xung_quanh(a, h)
        dien_tich_toan_phan = tinh_dien_tich_toan_phan(a, h)
        the_tich = tinh_the_tich(a, h)

        print("Diện tích xung quanh của hình chóp tứ giác đều là:", round(dien_tich_xung_quanh, 2))
        print("Diện tích toàn phần của hình chóp tứ giác đều là:", round(dien_tich_toan_phan, 2))
        print("Thể tích của hình chóp tứ giác đều là:", round(the_tich, 2))
    except ValueError:
        print("Vui lòng nhập số.")

if __name__ == "__main__":
    main()