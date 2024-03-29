#a
a = 0
for i in range(100, 1001):
  is_prime = True
  for d in range(2, int(i**0.5) + 1):
    if i % d == 0:
      is_prime = False
      break
  if is_prime:
    a += i

print("a)", a)
#b
for i in range(1,round(1000**0.5)):
    print("b)",i**2)
#c
a, b = 0, 1
for i in range (100):
    print("c)",a)
    a, b = b, a + b
    if a > 100 :
        break    
#d
for i in range(2, 500):
  d = 0
  for v in range(1, i):
    if i % v == 0:
      d += v
  if d == i:
    print("d)",i)
#e
e = 0
for i in range(1, 12):
    e += (i * (3 * i - 1)) / 2
print("e)",e) 