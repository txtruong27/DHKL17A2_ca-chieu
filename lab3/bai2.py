#a
a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        a += i
print(a)
#b
b=0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        b += i

print(b)