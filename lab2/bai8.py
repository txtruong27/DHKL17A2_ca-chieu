# Nhập đường thẳng thứ nhất
print("Nhập thông số của đường thẳng thứ nhất:")
a = float(input("Nhập hệ số góc (a): "))
b = float(input("Nhập hệ số tự do (b): "))

# Nhập đường thẳng thứ hai
print("\nNhập thông số của đường thẳng thứ hai:")
c = float(input("Nhập hệ số góc (c): "))
d = float(input("Nhập hệ số tự do (d): "))
# Kiểm tra 
if a == c:
    print("\nHai đường thẳng là đường thẳng song song hoặc trùng nhau.")
elif a * c == -1:
    print("\nHai đường thẳng là đường thẳng vuông góc.")
else:
    print("\nHai đường thẳng cắt nhau.")
