# Nhập số
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))

# Tính số BMI
bmi = can_nang / (chieu_cao ** 2)
# Phân loại số BMI
if bmi < 18.5:
    phan_loai = "Gầy"
elif bmi < 25:
    phan_loai = "Bình thường"
elif bmi < 30:
    phan_loai = "Hơi béo"
else:
    phan_loai = "Béo"
# In ra
print("Chỉ số BMI của bạn là:", bmi)
print("Phân loại BMI của bạn là:", phan_loai)
