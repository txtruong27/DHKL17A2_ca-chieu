chuoi_ban_dau = input("Nhập chuỗi ban đầu: ")
chuoi_da_sua = input("Nhập chuỗi đã sửa: ")
do_dai_ban_dau = len(chuoi_ban_dau)
do_dai_da_sua = len(chuoi_da_sua)
if abs(do_dai_da_sua - do_dai_ban_dau) > 1:
    print("Không thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")
else:
    if do_dai_da_sua == do_dai_ban_dau:
        so_luong_ky_tu_khac_nhau = sum(1 for ky_tu_ban_dau, ky_tu_da_sua in zip(chuoi_ban_dau, chuoi_da_sua) if ky_tu_ban_dau != ky_tu_da_sua)
        if so_luong_ky_tu_khac_nhau == 1:
            print("Có thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")
        else:
            print("Không thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")
    else:
        if do_dai_da_sua > do_dai_ban_dau:
            so_luong_ky_tu_khac_nhau = sum(1 for ky_tu_ban_dau, ky_tu_da_sua in zip(chuoi_ban_dau, chuoi_da_sua) if ky_tu_ban_dau != ky_tu_da_sua)
            if so_luong_ky_tu_khac_nhau <= 1:
                print("Có thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")
            else:
                print("Không thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")
        else:
            so_luong_ky_tu_khac_nhau = sum(1 for ky_tu_ban_dau, ky_tu_da_sua in zip(chuoi_ban_dau, chuoi_da_sua) if ky_tu_ban_dau != ky_tu_da_sua)
            if so_luong_ky_tu_khac_nhau <= 1:
                print("Có thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")
            else:
                print("Không thể thay đổi chuỗi ban đầu thành chuỗi đã sửa bằng cách thêm, xóa hoặc thay đổi một số ký tự.")

