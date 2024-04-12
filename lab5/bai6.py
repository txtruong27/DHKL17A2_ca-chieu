chuoi = input("Nhập chuỗi: ")
a = {}
total_chars = 0
for char in chuoi:
    if not char.isalnum():
        total_chars += 1
        if char in a:
            a[char] += 1
        else:
            a[char] = 1
b = {}
for char, count in a.items():
    p = (count / total_chars) * 100
    b[char] = p
print("Các ký tự đặc biệt trong chuỗi và số lần xuất hiện của chúng:")
for char, count in a.items():
    print(f"'{char}': {count} lần")

print("\nTỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi:")
for char, percentage in b.items():
    print(f"'{char}': {percentage:.2f}%")
