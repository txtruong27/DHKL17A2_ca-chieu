while True:
    x = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")
    if len(x) > 10:
        break
    else:
        print("Độ dài của chuỗi phải lớn hơn 10 ký tự. Vui lòng nhập lại.")

a = x[1:8]

b = x[4:9]

c = x[-3:]

d = x.lower()

e = x.upper()

f = x[::-1]

print("a) Chuỗi ký tự con từ vị trí 2 đến vị trí 8:", a)
print("b) Chuỗi ký tự con gồm 5 ký tự kể từ vị trí 5:", b)
print("c) Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", c)
print("d) Chuỗi chữ thường:", d)
print("e) Chuỗi chữ hoa:", e)
print("f) Chuỗi đảo ngược:", f)
