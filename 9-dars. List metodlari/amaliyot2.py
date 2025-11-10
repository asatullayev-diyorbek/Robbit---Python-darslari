davlatlar = ["O'zbekiston", "Germaniya", "Italiya", "Canada", "Meksika", "Yaponiya", "Turkiya"]

print(f"Mavjud davlatlar: {davlatlar}")

del davlatlar[3]
del davlatlar[5]

print(f"Qolgan davlatlar: {davlatlar}")

davlat = input("Davlat nomini kiriting: ")

if davlat in davlatlar:
    davlatlar.remove(davlat)
else:
    print("Bunday davlat topilmadi!")

print(f"Qolgan davlatlar: {davlatlar}")