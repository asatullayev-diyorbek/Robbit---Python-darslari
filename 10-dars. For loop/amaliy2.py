yoshlar = [12, 8, 9, 11, 15]
teens = []
kids = []

for yosh in yoshlar:
    if yosh >= 12:
        teens.append(yosh)
    else:
        kids.append(yosh)

print(f"Kids: {kids}")
print(f"Teen: {teens}")