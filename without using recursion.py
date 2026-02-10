#1RUA25BCA0012 - BALAJI K
n = int(input("Enter limit: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
