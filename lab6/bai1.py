n = int(input("Nhập số phần tử của mảng: "))
a = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(num)

chan = 0
le = 0
for num in a:
    if num % 2 == 0:
        chan += num
    else:
        le += num

print(f"Tổng các số chẵn trong mảng: {chan}")
print(f"Tổng các số lẻ trong mảng: {le}")
