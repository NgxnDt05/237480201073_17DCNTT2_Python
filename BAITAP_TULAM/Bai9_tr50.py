SoTien = int(input("Nhập số tiền: "))
MenhGia = [50000, 20000, 10000, 5000, 2000, 1000]
print("Tính số tờ tiền:")
for i in MenhGia:
    SoTo = SoTien // i
    if SoTo > 0:
        print(SoTo, "tờ", i)
    SoTien = SoTien % i
if SoTien > 0:
    print("Số tiền còn dư không chia hết cho 1000:", SoTien)