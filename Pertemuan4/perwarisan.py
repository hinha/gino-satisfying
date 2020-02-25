class Hero:

    def __init__(self, name, age, jumlah=10, hobi=""):
        self.name = name
        self.age = age
        self.hobi = hobi
        self.jumlah = jumlah

    def profil(self):
        print("Hi, i am " + self.name + " and ",  self.age,  " years old ")
        print("")

class Hero2:
    def __init__(self):
        pass
    
    def panggil_nama(self):
        print("Hero2")

class AnakHero(Hero, Hero2):
    
    def ubah_nama(self):
        self.name = "Anak Hijau"
        print(self.name)

    def hobi(self, data):
        print(data)

hero = Hero("Power Merah", 27, hobi="Bola")
hero2 = Hero2()
anakHero = AnakHero("Anak Merah", 5, hobi="Badminton")



hero.profil()
anakHero.profil()

print(hero.hobi)
print(anakHero.hobi)
print(anakHero.panggil_nama())

anakHero.ubah_nama()


cthHero = Hero("Phoenix", 20, jumlah=100)
print(cthHero.hobi)
print(cthHero.jumlah)
# anakHero.hobi("Badminton")