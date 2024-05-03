def t(N):
    return {x: x**3 for x in range(1, N+1)}
if __name__ == "__main__":
    N = int(input("Nhập vào số nguyên N: "))
    Ta_Xuan_Truong = t(N)
    print(Ta_Xuan_Truong)