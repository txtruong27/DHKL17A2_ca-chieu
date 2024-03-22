# Dictionary chứa cách đọc của các chữ số từ 0 đến 19
units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# Dictionary chứa cách đọc của các chữ số hàng chục
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# Dictionary chứa cách đọc của các số hàng trăm
hundreds = ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

# Nhập số nguyên từ người dùng
number = int(input("Nhập một số nguyên có ba chữ số: "))

# Tách các chữ số
digit_1 = number // 100
digit_2 = (number % 100) // 10
digit_3 = number % 10

# In ra cách đọc của số nguyên này theo tiếng Anh
print("Cách đọc của số nguyên này là:", end=" ")

if digit_1 != 0:
    print(hundreds[digit_1 - 1], end=" ")

if digit_2 != 0:
    if digit_2 == 1:
        print(units[number % 100], end=" ")
    else:
        print(tens[digit_2 - 2], end=" ")

if digit_3 != 0 and digit_2 != 1:
    print(units[digit_3])
elif digit_3 != 0 and digit_2 == 1:
    pass
else:
    print()
