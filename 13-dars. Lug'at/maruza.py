valyutalar = {'usd': 11900, 'rubl': 172}

print(valyutalar['rubl'])

# qo'shish yoki o'zgartirish
valyutalar['euro'] = 13800
print(valyutalar)

# o'chirish
del valyutalar['rubl']

print(valyutalar)

# tekshirish
if 'euro' in valyutalar.keys():
    print("Bor")
else:
    print("Yo'q")

for valyuta in valyutalar:
    print(valyuta)


# .keys()
# lug'at ichidan barcha kalitlarni olib beradi
print(valyutalar.keys())

# .values()
# lug'at ichidan barcha qiymatlarni olib beradi
print(valyutalar.values())

# .items()
# lug'at ichidan kalit va qiymatni birdek olib beradi
print(valyutalar.items())

print(valyutalar.get('rubl', "Bunday valyuta yo'q"))

