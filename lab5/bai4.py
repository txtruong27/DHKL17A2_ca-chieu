chuoi_dau_vao = input("Nhập chuỗi ký tự: ")
chuoi_so= ''.join(filter(str.isdigit, chuoi_dau_vao))
if chuoi_so:
    so = int(chuoi_so)
    if so <= 1:
        is_prime = False
    elif so <= 3:
        is_prime = True
    elif so % 2 == 0 or so % 3 == 0:
        is_prime = False
    else:
        is_prime = True
        i = 5
        while i * i <= so:
            if so % i == 0 or so % (i + 2) == 0:
                is_prime = False
                break
            i += 6
    if is_prime:
        print(f"Chuỗi ký tự '{chuoi_so}' là số nguyên tố.")
    else:
        print(f"Chuỗi ký tự '{chuoi_so}' không phải là số nguyên tố.")
else:
    print("Không có số trong chuỗi ký tự đã nhập.")
