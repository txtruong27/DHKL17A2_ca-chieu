str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

len1 = len(str1)
len2 = len(str2)

chuoi_hon_hop = []

max_len = max(len1, len2)

for i in range(max_len):
    if i < len1:
        chuoi_hon_hop.append(str1[i])
    if i < len2:
        chuoi_hon_hop.append(str2[i])

result = '-'.join(chuoi_hon_hop)
print("Chuỗi kết quả sau khi trộn là:", result)
