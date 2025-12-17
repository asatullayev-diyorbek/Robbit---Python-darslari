# 245, 2 -> 2245
# 546, 7 -> 7546

def AddLeftDigit(K, R):
    K2 = K
    xona_soni = 0
    while K2 > 0:
        xona_soni+=1
        K2 = K2 // 10
    return R * 10**xona_soni + K

print(AddLeftDigit(256, 3))