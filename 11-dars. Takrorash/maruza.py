# random
import random

son = random.randint(1, 10)

print(f"Son: {son}")

mevalar = ['olma', 'behi', 'anor', 'chirigan', 'uzum', 'banan']
tanlangan_meva = random.choice(mevalar)

print(f"Tanlangan meva: {tanlangan_meva}")

# break
for meva in mevalar:
    if meva == 'chirigan':
        print("Topildi")
        break
    
    print(meva)

print("Tugadi")

# continue
for meva in mevalar:
    if meva == 'chirigan':
        print("Topildi")
        continue
    
    print(meva)

print("Tugadi")