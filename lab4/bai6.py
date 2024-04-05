so_va_chu = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}
so = input("Nhập một số: ")
ket_qua = ""
for chu in so:
    ket_qua += so_va_chu.get(chu, '') + ' '
print("Kết quả in ra màn hình là:", ket_qua.strip())
