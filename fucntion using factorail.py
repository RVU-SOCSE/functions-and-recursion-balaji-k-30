#1RUA25BCA0012_BALAJI K
def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    print(f'factorial for {n} is {f}')

n=int(input("ENTER AN NUMBER:"))
fact(n)
