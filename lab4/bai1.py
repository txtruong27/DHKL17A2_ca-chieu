so = []
a = 0
print("Nhập các số nguyên dương từ bàn phím (nhập 'q' để kết thúc):")
while a <= 1000:
    num_input = input("Nhập số nguyên dương: ")
    if num_input.lower() == 'q':
        break
    num = int(num_input)
    if num <= 0:
        print("Vui lòng nhập một số nguyên dương.")
        continue
    so.append(num)
    a += num
so_le = [num for num in so if num % 2 != 0]
so_chan = [num for num in so if num % 2 == 0]
print("Các số lẻ đã nhập là:", " ".join(map(str, so_le)))
print("Các số chẵn đã nhập là:", " ".join(map(str, so_chan)))
print("Số lượng các số nguyên đã nhập:", len(so))
