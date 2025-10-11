a, b, c = eval(input('Nhap vao 3 so cach nhau boi dau phay: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
        print('Day la tam giac vuong')
    elif a == b == c:
        print('Day la tam giac deu')
    elif a == b or a == c or b == c:
        print('Day la tam giac can')
else:
    print("Ba gia tri vua nhap khong la 1 tam giac!")