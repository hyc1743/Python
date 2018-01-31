import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float))|isinstance(b,(int,float))|isinstance(c,(int,float)):
        raise TypeError('输入数据错误！')

delt = b*b-(4*a*c)
print(delt)

if delt>=0:
    p = -(b/(2*a))
    q = math.sqrt(delt)/(2*a)

    if delt == 0:
        print("x1=x2=%f" % p)
    else:
        x1=p+q
        x2=p-q
        print("x1=%f,x2=%f" % (x1,x2))

else:

    print("没有实根！")
    
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))

quadratic(a,b,c)