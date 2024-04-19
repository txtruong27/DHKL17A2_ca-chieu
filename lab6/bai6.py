m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(float(input(f"Nhập phần tử [{i+1}, {j+1}]: ")))
    ma_tran.append(hang)

tong = 0
for hang in ma_tran:
    tong += sum(hang)
print("Tổng các phần tử trong ma trận:", tong)

m2 = int(input("Nhập số hàng của ma trận thứ hai: "))
n2 = int(input("Nhập số cột của ma trận thứ hai: "))
ma_tran2 = []
for i in range(m2):
    hang = []
    for j in range(n2):
        hang.append(float(input(f"Nhập phần tử [{i+1}, {j+1}] của ma trận thứ hai: ")))
    ma_tran2.append(hang)

if n != m2:
    print("Không thể nhân hai ma trận này.")
else:
    ma_tran2_chuyen_vi = [[ma_tran2[j][i] for j in range(len(ma_tran2))] for i in range(len(ma_tran2[0]))]
    ma_tran_tich = [[sum(x * y for x, y in zip(hang1, cot2)) for cot2 in ma_tran2_chuyen_vi] for hang1 in ma_tran]
    print("Tích của hai ma trận:")
    for hang in ma_tran_tich:
        print(hang)

ma_tran_chuyen_vi = [[ma_tran[j][i] for j in range(len(ma_tran))] for i in range(len(ma_tran[0]))]
print("Ma trận chuyển vị:")
for hang in ma_tran_chuyen_vi:
    print(hang)