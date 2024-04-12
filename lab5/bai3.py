chuoi_van_ban = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm: ")
vi_tri = chuoi_van_ban.find(tu_can_tim)
print("Vị trí của từ cần tìm trong chuỗi:", vi_tri)
danh_sach_tu = chuoi_van_ban.split()
dem_tu = {}
for tu in danh_sach_tu:
    if tu in dem_tu:
        dem_tu[tu] += 1
    else:
        dem_tu[tu] = 1
tu_nhieu_nhat = max(dem_tu, key=dem_tu.get)


print("Từ xuất hiện nhiều nhất trong chuỗi là:", tu_nhieu_nhat)
print("Số lần xuất hiện của từ đó:", dem_tu[tu_nhieu_nhat])
