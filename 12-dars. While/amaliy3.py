import random

ball = 0

while -5 < ball < 10:
	son1 = random.randint(10, 100)
	son2 = random.randint(10, 100)

	javob = int(input(f"{son1} + {son2} = "))

	if son1 + son2 == javob:
		ball += 1
		print("To'g'ri javob!")
	else:
		ball -= 1
		print("Noto'g'ri javob")

	print(f"Sizning balingiz: {ball}")

if ball >= 10:
	print("Siz yutdingiz!")
else:
	print("Siz yutqazdingiz!")
