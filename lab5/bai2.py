
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
len1 = len(str1)
len2 = len(str2)
x = [[0] * (len2 + 1) for _ in range(len1 + 1)]
min_length = float('inf')
end_index = 0
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            x [i][j] = x [i - 1][j - 1] + 1
            if x[i][j] < min_length:
                min_length = x[i][j]
                end_index = i
chuoi_ki_tu = str1[end_index - min_length:end_index]
if chuoi_ki_tu:
    print("Chuỗi ký tự con chung có độ dài ngắn nhất:", chuoi_ki_tu)
else:
    print("Không có chuỗi ký tự con chung.")
