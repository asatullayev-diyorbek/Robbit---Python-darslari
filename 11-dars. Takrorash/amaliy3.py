import random

print("*** Number guessing game ***")
print("Kompyuter o'ylagan sonni 3ta uirinishda topishingiz kerak!")

random_son = random.randint(1, 10)

for i in range(1, 4):
    kiritilgan_son = int(input(f"{i}-urinish - Son kiriting: "))

    if random_son < kiritilgan_son:
        print("Men o'ylagan son kichikroq")
    
    elif random_son > kiritilgan_son:
        print("Men o'ylagan son kattaroq")
    
    else:
        print(f"🎁 Tabriklaymiz, o'ylangan sonni {i} ta urinishda topdingiz")
        break
else:
    print("Siz yutqazdingiz")


