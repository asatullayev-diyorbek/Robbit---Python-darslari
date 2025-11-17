# n butun son berilgan, quyidagi yig'indini hisoblovchi programma tuzilsin
# S = 1 + 1/2 + 1/3 + .. + 1/n 

n = int(input("n = "))
s = 0

for i in range(1, n+1):
    s += 1/i
print(f"S = {s}")