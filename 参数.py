def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
x=int(input(''))
n=int(input(''))
print(power(x,n))