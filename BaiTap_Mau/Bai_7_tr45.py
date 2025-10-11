a = int(input('Nhap vao so nguyen duong a: '))
b = int(input('Nhap vao so nguyen duong b: '))
c = int(input('Nhap vao so nguyen duong c: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Ba gia tri vua nhap la 1 tam giac!')
else:
    print("Ba gia tri vua nhap khong la 1 tam giac!")