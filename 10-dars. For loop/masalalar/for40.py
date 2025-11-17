# A va B butun sonlar beriladi
# A va B sonlar orasidagi barcha butun sonlarni ekranga chiqarish kerak
# A
# A+1 A+1
# A+2 A+2 A+2
# A+3 A+3 A+3 A+3

a = int(input("a = "))
b = int(input("b = "))

count = 1
for i in range(a, b+1):
    for j in range(count):
        print(i, end=' ')
    count += 1
    print()