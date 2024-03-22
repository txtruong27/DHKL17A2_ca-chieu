# Dictionary chứa thông tin về thời gian chiếu của từng thể loại phim
thoi_gian_chieu = {
    'Hành động': ['Sáng', 'Trưa', 'Chiều', 'Tối'],
    'Kinh dị': ['Tối'],
    'Tình cảm': ['Tối'],
    'Hài hước': ['Sáng', 'Trưa', 'Chiều', 'Tối'],
    'Hoạt hình': ['Sáng', 'Trưa']
}

# Hiển thị danh sách các thể loại phim
print("Danh sách các thể loại phim:")
for index, the_loai in enumerate(thoi_gian_chieu.keys(), start=1):
    print(f"{index}. {the_loai}")

# Yêu cầu người dùng nhập lựa chọn thể loại phim
lua_chon_the_loai = int(input("\nNhập số thứ tự của thể loại phim bạn muốn xem: "))

# Kiểm tra nếu lựa chọn của người dùng nằm ngoài phạm vi
if lua_chon_the_loai < 1 or lua_chon_the_loai > len(thoi_gian_chieu):
    print("Lựa chọn không hợp lệ.")
else:
    # Chuyển đổi lựa chọn thành tên thể loại phim
    danh_sach_the_loai = list(thoi_gian_chieu.keys())
    the_loai_chon = danh_sach_the_loai[lua_chon_the_loai - 1]

    # Yêu cầu người dùng nhập thời gian muốn xem phim
    print(f"\nBạn đã chọn thể loại phim: {the_loai_chon}")
    print("Thời gian chiếu phim cho thể loại này là:", ", ".join(thoi_gian_chieu[the_loai_chon]))

    thoi_gian_muon_xem = input("\nNhập thời gian muốn xem phim (Sáng/Trưa/Chiều/Tối): ")

    # Kiểm tra xem thời gian muốn xem có phù hợp không
    if thoi_gian_muon_xem not in thoi_gian_chieu[the_loai_chon]:
        print("Không có suất chiếu cho thời gian này.")
    else:
        print(f"Bạn đã chọn xem phim {the_loai_chon} vào thời gian {thoi_gian_muon_xem}.")
