n = int(input("Nhập số nguyên dương n: "))
if n % 5 == 0 and n % 7 == 0:
    print(n,"Có thể chia hết cho cả 5 và 7")
else:
    print(n,"Không thể chia hết cho cả 5 và 7")