a,b = map(int,input("Nhập vào hệ số của phương trình: ").split())
print("Phương trình bạn đã nhập là: {}x + {} = 0".format(a, b))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print("Nghiệm của phương trình là:", x)
