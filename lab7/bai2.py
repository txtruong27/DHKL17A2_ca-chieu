def xep_loai(diem):
    if diem < 4.0:
        return 'F' 
    elif 4.0 <= diem <= 5.4:
        return 'D'
    elif 5.5 <= diem <= 6.9:
        return 'C'
    elif 7.0 <= diem <= 8.4:
        return 'B'
    else:
        return 'A'
if __name__ == "__main__":
    thong_tin_sinh_vien = {}
    thong_ke_hoc_luc = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for i in range(10):
        ten,diem = input(f"Nhập tên sinh viên thứ {i+1}: "),float(input("Nhập điểm thi: "))
        loai = xep_loai(diem)
        thong_tin_sinh_vien[ten] = {'Điểm': diem, 'Xếp loại': loai}
        thong_ke_hoc_luc[loai] += 1
    print("\nThông tin và xếp loại học lực của sinh viên:")
    for ten, info in thong_tin_sinh_vien.items():
        print(f"{ten}: Điểm - {info['Điểm']}, Xếp loại - {info['Xếp loại']}")
    print("\nThống kê số lượng sinh viên theo học lực:")
    for loai, so_luong in thong_ke_hoc_luc.items():
        print(f"Học lực {loai}: {so_luong} sinh viên")