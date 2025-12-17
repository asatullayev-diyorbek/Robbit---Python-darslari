class Speaker:
    def __init__(self, name, music):
        self.name = name
        self.music = music
    
class Car:
    def __init__(self, name, color, max_speed, speaker):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.speaker = speaker
    
    def __str__(self):
        return f"{self.name} - {self.max_speed} km/h"

    def info(self):
        print("*** Mashina ma'lumotlari ***")
        print(f"Nomi: {self.name}")
        print(f"Rangi: {self.color}")
        print(f"Maks. Tezligi: {self.max_speed}")

    def play_music(self):
        print("Musiqa qo'yilmoqda....")
        print(f"Music name: {self.speaker.music}")

speaker1 = Speaker("Pioneer", "Ko'k jiguli")
car1 = Car("Matiz", "Yashil", 160, speaker1)

car1.info()

car1.play_music()

# Topshiriq. Mashina ishlab chiqarilgan yilini ham saqlash kerak
# info_year() metodi qo'shilsin. U mashina ishlab chiqarilganiga necha yil bo'lganini aytsin