def dem_tu(van_ban):
    tu_dem = {}
    for tu in van_ban.split():
        if tu in tu_dem:
            tu_dem[tu] += 1
        else:
            tu_dem[tu] = 1
    tu_nhieu_nhat = max(tu_dem, key=tu_dem.get)
    tu_it_nhat = min(tu_dem, key=tu_dem.get)
    return tu_nhieu_nhat, tu_dem[tu_nhieu_nhat], tu_it_nhat, tu_dem[tu_it_nhat]
if __name__ == "__main__":
    van_ban = """Dog is a pet animal It is the oldest friend of human beings
             It watches our house 
             It is very faithful animal and never left his master
             It is used by police to fight crime Sheep- rearers also use them.
             Thus it is useful for us in many ways"""
    tu_nhieu_nhat, so_lan_nhieu_nhat, tu_it_nhat, so_lan_it_nhat = dem_tu(van_ban)
    
    print(f"Từ xuất hiện nhiều nhất: '{tu_nhieu_nhat}' với {so_lan_nhieu_nhat} lần.")
    print(f"Từ xuất hiện ít nhất: '{tu_it_nhat}' với {so_lan_it_nhat} lần.")