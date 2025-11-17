# 1kga konfet narxi berilgan. 
# Siz 0.1, 0.2, ..., 0.9, 1.0kg konfet narxlarini chiqarishingiz kerak

narx = int(input("1kg konfet narxini kiriting: "))

for i in range(1, 11):
    print(f"{i/10} kg konfet narxi: {i/10 * narx} so'm")