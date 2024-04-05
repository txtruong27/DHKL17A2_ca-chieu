n = int(input("nhập só nguyên lớn hơn 10 :")) 
a = 1
S1=S2=S3=S4=0
while n <= 10:
    n = int(input("Bạn vừa nhập sai. Vui lòng nhập số nguyên lớn hơn 10 :")) 
while a <= n :
       S1 += 6**a
       S2 += (1/3)**(2*a-1)
       S3 += (a**2)*(-1)**a
       S4 += (a+1)*(a+2)*a
       a += 1
print("a)  S1 = ", S1)
print("b)  S2 = ", S2)
print("c)  S3 = ", S3)
print("d)  S4 = ", S4)