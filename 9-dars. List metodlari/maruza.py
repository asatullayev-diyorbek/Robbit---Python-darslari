bozorlik = ['kartoshka', 'piyoz', 'tuz', "yog'"]
mevalar = ['olma', 'behi', 'olma', 'anor', 'nok']


bozorlik.insert(3, "sabzi")  # list ning berilgan index iga element qo'shib beradi
bozorlik.append('pomidor') # listning oxiriga element qo'shadi

print(bozorlik)
print(len(bozorlik))


# mevalar.remove("olma")  # element qiymati bo'yicha o'chiradi

del mevalar[2]  # element index bo'yicha o'chiradi

print(mevalar)

if 'olma' in mevalar:  # in - ro'yxat ichidan bor yoki yo'qligini tekshirib beradi
    print("Bor")
else:
    print("Yo'q")

yangi_meva = []

# pop - berilgan index dagi elementni sug'irib oladi. pop() deb ishlatsak oxiridagi elementni oladi
yangi_meva.append(mevalar.pop()) 
yangi_meva.append(mevalar.pop(2))

print(mevalar)
print(yangi_meva)

# count() - list ichida elementni nechta borligini aniqlab beradi

ism = "Toshpo'lat"

print(ism.count('9'))


# sort - tartiblab beradi

mevalar = ['olma', 'behi', 'olma', 'anor', 'nok']
# mevalar.sort(reverse=True)
mevalar.reverse()
print(mevalar)

