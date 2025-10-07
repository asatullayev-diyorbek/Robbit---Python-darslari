uzim = 21
muzaffarxon_yoshi = 13
shohjahon_yoshi = 12
muhammadaziz_yoshi = 13
adhamjon_yoshi = 13
abdurahmon_yoshi = 15
abduqodir_yoshi = 15

kichik_yosh = min(
    uzim, muhammadaziz_yoshi, shohjahon_yoshi,
    muzaffarxon_yoshi,adhamjon_yoshi, 
    abduqodir_yoshi, abdurahmon_yoshi
)
katta_yosh = max(
    uzim, muhammadaziz_yoshi, shohjahon_yoshi,
    muzaffarxon_yoshi,adhamjon_yoshi, 
    abduqodir_yoshi, abdurahmon_yoshi
)
urtacha_yosh = (uzim + muzaffarxon_yoshi + shohjahon_yoshi 
                + muhammadaziz_yoshi + adhamjon_yoshi + 
                abduqodir_yoshi + abdurahmon_yoshi) / 7

print(f"Eng kichik yosh: {kichik_yosh}")
print(f"Eng katta yosh: {katta_yosh}")
print(f"O'rtacha yosh: {urtacha_yosh}")