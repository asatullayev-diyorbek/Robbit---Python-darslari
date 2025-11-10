# chips, krieshki, cola, pepsi, marshmello, yogurt

# list - ro'yxat

# sweets = ['chips', 'krieshki', 'cola', 'pepsi', 15, 16.7, True, 2j+1]

# print(sweets) # string uchun

# sweets[1] = 'kereshki'

# print(len(sweets))

# sweets.append('to\'rt')

# print(sweets)

# sonlar = [15, 26, 75, 89]

# print(min(sonlar))
# print(max(sonlar))
# print(sum(sonlar))
# print(sum(sonlar) / len(sonlar))


# 1 ---------
# sonlar = []
# son = int(input("Sonni kiriting: "))
# sonlar.append(son)
# son = int(input("Sonni kiriting: "))
# sonlar.append(son)
# son = int(input("Sonni kiriting: "))
# sonlar.append(son)


# print(sonlar)

# 2 ------------
# sonlar = input("Sonlarni kiriting: ").split(' ')
# print(int(sonlar[1]) + int(sonlar[3]))
# print(sonlar)


# 3 ------------
sonlar = list(map(int, input("Sonlarni kiriting: ").split(' ')))
# print(sonlar[1] + sonlar[3])
sonlar.reverse()
print(sonlar)
