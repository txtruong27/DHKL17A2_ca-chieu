numbers = input("Nhập dãy số, cách nhau bằng khoảng trắng: ").split()

numbers = [float(num) for num in numbers]

max_number = max(numbers)
min_number = min(numbers)

print(f"Số lớn nhất trong dãy số là: {max_number}")
print(f"Số nhỏ nhất trong dãy số là: {min_number}")
