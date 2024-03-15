def tinh_tien_dien(gio_su_dung):
    # Công suất của máy lọc không khí (P) được tính bằng tích của hiệu điện thế (U) và cường độ dòng điện (I)
    cong_suat = 220 * 1.5  # Đơn vị: W (Watt)
    
    # Đổi đơn vị từ Watt sang kWh (Kilowatt-hour)
    cong_suat_kwh = cong_suat / 1000  # Đơn vị: kWh
    
    # Tính tổng số điện tiêu thụ
    dien_tieu_thu = cong_suat_kwh * gio_su_dung  # Đơn vị: kWh
    
    # Giá điện là 5000 đồng/kWh
    gia_dien = 5000  # Đơn vị: đồng
    
    # Tính tổng số tiền điện phải trả
    tien_dien = dien_tieu_thu * gia_dien  # Đơn vị: đồng
    
    return tien_dien

def main():
    try:
        gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))
        
        if gio_su_dung <= 0:
            print("Số giờ sử dụng phải lớn hơn 0.")
        else:
            tien_dien = tinh_tien_dien(gio_su_dung)
            print(f"Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí trong {gio_su_dung} giờ là: {tien_dien} đồng")
    except ValueError:
        print("Vui lòng nhập số giờ sử dụng là một số thực.")

if __name__ == "__main__":
    main()