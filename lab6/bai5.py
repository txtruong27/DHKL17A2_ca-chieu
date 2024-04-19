chuoi_so = input("Nhập dãy số, cách nhau bằng khoảng trắng: ").split()

chuoi_so = [int(num) for num in chuoi_so]

la_cac_so_tiep_hang = True
if len(chuoi_so) > 1:
    hieu_chung = chuoi_so[1] - chuoi_so[0]
    for i in range(2, len(chuoi_so)):
        if chuoi_so[i] - chuoi_so[i - 1] != hieu_chung:
            la_cac_so_tiep_hang = False
            break

if la_cac_so_tiep_hang:
    print("Dãy số tạo thành cấp số cộng:", chuoi_so)
else:
    print("Dãy số không tạo thành cấp số cộng.")
