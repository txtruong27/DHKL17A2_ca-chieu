#6.1
def loc_so_le(danh_sach):
    return list(filter(lambda x: x % 2 != 0, danh_sach))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Các số lẻ trong danh sách:", loc_so_le(danh_sach))
#6.2
def loc_so_chan(danh_sach):
    return list(filter(lambda x: x % 2 == 0, danh_sach))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Các số chẵn trong danh sách:", loc_so_chan(danh_sach))
#6.3
def lap_phuong(danh_sach):
    return list(map(lambda x: x ** 3, danh_sach))

danh_sach = [1, 2, 3, 4, 5]
print("Danh sách lập phương của các phần tử trong danh sách ban đầu:", lap_phuong(danh_sach))
#6.4
def lap_phuong_so_chan(danh_sach):
    return list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, danh_sach)))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Danh sách lập phương của các số chẵn trong danh sách:", lap_phuong_so_chan(danh_sach))
#6.5
def binh_phuong_so_le(danh_sach):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, danh_sach)))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Danh sách bình phương của các số lẻ trong danh sách:", binh_phuong_so_le(danh_sach))


