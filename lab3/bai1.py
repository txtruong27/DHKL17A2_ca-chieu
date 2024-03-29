#a
a = int(input("nhap so nguyên duong :"))
b = 0
if a <= 0:
    a = int(input("số vừa nhập không đúng,vui lòng nhập lại :"))
for i in range(1,a+1):
    b += i 
print(b)    
#b
a = int(input("nhap so nguyên duong :"))
b = 0
if a <= 0:
    a = int(input("số vừa nhập không đúng,vui lòng nhập lại :"))
for i in range(1,a+1):
    b += 1/i
print(b) 
#c
a = int(input("nhap so nguyên duong :"))
b = 0
if a <= 0:
    a = int(input("số vừa nhập không đúng,vui lòng nhập lại :"))
for i in range(1,a+1):
    b += 1/(i*2)**0.5 
print(b) 
#d
a = int(input("nhap so nguyên duong :"))
b = 0
if a <= 0:
    a = int(input("số vừa nhập không đúng,vui lòng nhập lại :"))
for i in range(1,a+1):
    b += (-1/i)**(i+1)
print(b) 