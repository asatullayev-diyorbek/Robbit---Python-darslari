bozorlik = ['kartoshka', 'piyoz', 'tuz', "yog'", "tuxum"]
olinganlar = []
olingan = input("Olingan mahsulotni kiriting: ")

if olingan in bozorlik:
    # print(f"Olingan indeksi: {bozorlik.index(olingan)}")
    olinganlar.append(bozorlik.pop(bozorlik.index(olingan)))
    print(f"Sotib olindi: {olingan}")
else:
    print("Bunday mahsulot mavjud emas!")

olingan = input("Olingan mahsulotni kiriting: ")

if olingan in bozorlik:
    # print(f"Olingan indeksi: {bozorlik.index(olingan)}")
    olinganlar.append(bozorlik.pop(bozorlik.index(olingan)))
    print(f"Sotib olindi: {olingan}")
else:
    print("Bunday mahsulot mavjud emas!")

print(f"Sotib olinmagan mahsulotlar: {bozorlik}")
print(f"Sotib olingan mahsulotlar: {olinganlar}")
