def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_sinh_doi():
    so_nguyen_to_sinh_doi_list = []
    for num in range(3, 1000, 2):
        if la_so_nguyen_to(num) and la_so_nguyen_to(num + 2):
            so_nguyen_to_sinh_doi_list.append((num, num + 2))
    return so_nguyen_to_sinh_doi_list

print("Các số nguyên tố sinh đôi nhỏ hơn 1000 là:")
for cap in so_nguyen_to_sinh_doi():
    print(cap)
